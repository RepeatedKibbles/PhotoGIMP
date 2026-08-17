#!/usr/bin/env python3
"""Upload release artifacts to VirusTotal and write a Markdown report."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request
import uuid

API = "https://www.virustotal.com/api/v3"


def request(path: str, api_key: str) -> dict:
    req = urllib.request.Request(f"{API}{path}", headers={"x-apikey": api_key})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)


def upload(path: Path, api_key: str) -> str:
    boundary = uuid.uuid4().hex
    data = path.read_bytes()
    body = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{path.name}\"\r\n"
        "Content-Type: application/octet-stream\r\n\r\n"
    ).encode() + data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        f"{API}/files",
        data=body,
        method="POST",
        headers={"x-apikey": api_key, "Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.load(response)["data"]["id"]


def wait_for_analysis(analysis_id: str, api_key: str) -> dict:
    for _ in range(30):
        result = request(f"/analyses/{analysis_id}", api_key)
        if result["data"]["attributes"]["status"] == "completed":
            return result["data"]["attributes"]["stats"]
        time.sleep(20)
    raise TimeoutError(f"VirusTotal analysis did not complete: {analysis_id}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    api_key = os.environ.get("VIRUSTOTAL_API_KEY")
    if not api_key:
        raise SystemExit("VIRUSTOTAL_API_KEY is required")

    rows = []
    failed = False
    for index, path in enumerate(args.files):
        if index:
            # Public API quotas are intentionally respected between artifacts.
            time.sleep(20)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        analysis_id = upload(path, api_key)
        stats = wait_for_analysis(analysis_id, api_key)
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        failed |= malicious > 0 or suspicious > 0
        rows.append((path.name, digest, malicious, suspicious, stats.get("undetected", 0)))

    lines = [
        "# VirusTotal release scan\n",
        "| Artifact | SHA-256 | Malicious | Suspicious | Undetected | Report |",
        "|---|---|---:|---:|---:|---|",
    ]
    for name, digest, malicious, suspicious, undetected in rows:
        lines.append(
            f"| `{name}` | `{digest}` | {malicious} | {suspicious} | {undetected} | "
            f"[VirusTotal](https://www.virustotal.com/gui/file/{digest}) |"
        )
    lines.append("\nA release is published only when all artifacts have zero malicious and suspicious detections.\n")
    args.report.write_text("\n".join(lines), encoding="utf-8")
    if failed:
        raise SystemExit("VirusTotal reported malicious or suspicious detections")


if __name__ == "__main__":
    main()
