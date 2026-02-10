# 🎨 PhotoGIMP

<img src="../.local/share/icons/hicolor/256x256/256x256.png" align="right" alt="Ícone do PhotoGIMP" title="Ícone do PhotoGIMP">

[![GitHub stars](https://img.shields.io/github/stars/Diolinux/PhotoGIMP?style=social)](https://github.com/Diolinux/PhotoGIMP)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Latest Release](https://img.shields.io/github/v/release/Diolinux/PhotoGIMP)](https://github.com/Diolinux/PhotoGIMP/releases/latest)

**PhotoGIMP** é um patch gratuito e mantido pela comunidade que transforma o [GIMP](https://www.gimp.org/) (GNU Image Manipulation Program) em um layout familiar para usuários do **Adobe Photoshop**. Se você está migrando do Photoshop para o GIMP e quer se sentir em casa imediatamente, o PhotoGIMP é para você.

> **Novo no GIMP?** O GIMP é um editor de imagens gratuito e de código aberto disponível para Linux, macOS e Windows. Ele pode fazer quase tudo que o Photoshop faz — retoque de fotos, composição de imagens, design gráfico e muito mais — tudo de graça. O PhotoGIMP apenas faz com que ele *pareça e funcione* mais como o Photoshop.

---

## ✨ Recursos

- **Layout de ferramentas no estilo Photoshop** — As ferramentas são reorganizadas para imitar as posições que você já conhece do Adobe Photoshop.
- **Tela Inicial personalizada** — Uma splash screen exclusiva do PhotoGIMP aparece ao iniciar o programa.
- **Espaço de trabalho maximizado** — As configurações padrão são otimizadas para dar a você a maior área de trabalho possível.
- **Atalhos de teclado do Photoshop** — Os atalhos seguem a [documentação oficial da Adobe](https://helpx.adobe.com/photoshop/using/default-keyboard-shortcuts.html) para a versão Windows.
- **Ícone e nome personalizados** — Um arquivo `.desktop` dedicado dá ao PhotoGIMP seu próprio ícone e nome no menu do sistema.

---

## 📷 Capturas de Tela

<p>
  <img src="../.config/GIMP/3.0/splashes/splash-screen-2025-v2.png" alt="PhotoGIMP Diolinux Splash Art">
  <em>PhotoGIMP Diolinux Splash Art</em>
</p>

<p>
  <img src="../screenshots/photogimp_3_-_diolinux.png" alt="PhotoGIMP 3">
  <em>GIMP 3.0 com o patch PhotoGIMP aplicado</em>
</p>

---

## 📋 Requisitos

Antes de instalar o PhotoGIMP, certifique-se de que você tem:

| Requisito | Detalhes |
|---|---|
| **GIMP 3.0 ou mais recente** | Baixe em: [gimp.org](https://www.gimp.org/downloads/) ou [Flathub](https://flathub.org/apps/org.gimp.GIMP) (Linux) |
| **Executar o GIMP pelo menos uma vez** | O GIMP precisa gerar seus arquivos de configuração antes que o PhotoGIMP possa sobrescrevê-los. **Instale o GIMP → abra-o → feche-o → depois instale o PhotoGIMP.** |

---

## ⚙ Como Instalar

> [!WARNING]
> **Faça backup das suas configurações atuais do GIMP antes de instalar!** O PhotoGIMP sobrescreve os arquivos de configuração do GIMP. Se você tem configurações personalizadas que deseja manter, salve uma cópia de backup primeiro. Veja as instruções de backup em cada seção abaixo.

---

### 🐧 Flatpak (Linux)

<img src="https://skillicons.dev/icons?i=linux" align="right" width="40" />

#### Backup (opcional)

Se você deseja manter suas configurações atuais do GIMP, faça o backup primeiro:

```bash
cp -r ~/.config/GIMP/3.0 ~/GIMP-3.0-backup
```

#### Instalação

1. Certifique-se de que o GIMP já está instalado [pelo Flathub](https://flathub.org/apps/org.gimp.GIMP).
2. **Abra o GIMP uma vez e depois feche-o** — isso cria as pastas de configuração que o PhotoGIMP precisa.
3. Baixe a versão mais recente:
   👉 **[Baixar PhotoGIMP para Linux (.zip)](https://github.com/Diolinux/PhotoGIMP/releases/download/3.0/PhotoGIMP-linux.zip)**
4. Extraia o arquivo `.zip` **na sua pasta pessoal** (`~`).
   - Isso colocará arquivos em `~/.config` e `~/.local`, que são pastas ocultas.
   - Para ver pastas ocultas no seu gerenciador de arquivos, pressione <kbd>Ctrl</kbd> + <kbd>H</kbd>.
   - Quando perguntado sobre arquivos existentes, escolha **"Substituir"** ou **"Sobrescrever"**.
5. Abra o GIMP — você deverá ver o novo layout do PhotoGIMP! 🎉

<details>
<summary><strong>💡 Usando um GIMP que não é Flatpak?</strong></summary>

Se você instalou o GIMP pelo gerenciador de pacotes da sua distribuição (apt, dnf, pacman, etc.) em vez do Flatpak, a pasta de configuração está no mesmo local (`~/.config/GIMP/3.0`), então os passos acima ainda funcionam. Apenas certifique-se de que você tem o GIMP versão 3.0 ou mais recente.
</details>

---

### 🪟 Windows

<img src="https://skillicons.dev/icons?i=windows" align="right" />

#### Backup (opcional)

Se você deseja manter suas configurações atuais do GIMP, faça o backup primeiro:

1. Pressione <kbd>Windows</kbd> + <kbd>R</kbd> para abrir o diálogo Executar.
2. Digite `%APPDATA%\GIMP` e pressione <kbd>Enter</kbd>.
3. Copie toda a pasta `3.0` para um local seguro (ex.: sua Área de Trabalho).

#### Instalação

1. Certifique-se de que o [GIMP está instalado pelo site oficial](https://www.gimp.org/downloads/).
2. **Abra o GIMP uma vez e depois feche-o** — isso cria as pastas de configuração que o PhotoGIMP precisa.
3. Baixe a versão mais recente:
   👉 **[Baixar PhotoGIMP para Windows (.zip)](https://github.com/Diolinux/PhotoGIMP/releases/download/3.0/PhotoGIMP.zip)**
4. Extraia o conteúdo de `PhotoGIMP.zip` para qualquer pasta (ex.: sua Área de Trabalho).
5. Abra a pasta extraída e **copie a pasta `3.0`**.
6. Pressione <kbd>Windows</kbd> + <kbd>R</kbd> para abrir o diálogo Executar.
7. Digite `%APPDATA%\GIMP` e pressione <kbd>Enter</kbd> — isso abre a pasta de configurações do GIMP.
8. **Cole** a pasta `3.0` aqui.
9. Quando perguntado sobre arquivos existentes, selecione **"Substituir os arquivos no destino"**.
10. Abra o GIMP — você deverá ver o novo layout do PhotoGIMP! 🎉

<details>
<summary><strong>💡 Opcional: Alterar o ícone do atalho do GIMP</strong></summary>

Você também pode baixar o [photogimp.ico](https://github.com/Diolinux/PhotoGIMP/releases/download/3.0/photogimp.ico) e atualizar o ícone no atalho do GIMP localizado em:

```
%appdata%\Microsoft\Windows\Start Menu\Programs\GIMP 3.0.0
```

Clique com o botão direito no atalho → **Propriedades** → **Alterar Ícone** → navegue até o arquivo `.ico` baixado.
</details>

<details>
<summary><strong>🍫 Instalar via Chocolatey (alternativa)</strong></summary>

Se você usa o [Chocolatey](https://chocolatey.org/), pode instalar o PhotoGIMP com um único comando:

```powershell
choco install photogimp
```

Mantido por: [André Augusto](https://github.com/AndreAugustoDev)
</details>

---

### 🍎 macOS

<img src="https://skillicons.dev/icons?i=macos" align="right" />

#### Backup (opcional)

Se você deseja manter suas configurações atuais do GIMP, faça o backup primeiro:

1. Abra o Finder.
2. Pressione <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> e vá para `~/Library/Application Support/GIMP`.
3. Copie toda a pasta `GIMP` para um local seguro (ex.: sua Área de Trabalho).

#### Instalação

1. Certifique-se de que o [GIMP está instalado pelo site oficial](https://www.gimp.org/downloads/).
2. **Abra o GIMP uma vez e depois feche-o** — isso cria as pastas de configuração que o PhotoGIMP precisa.
3. Baixe a versão mais recente:
   👉 **[Baixar PhotoGIMP para macOS (.zip)](https://github.com/Diolinux/PhotoGIMP/releases/download/3.0/PhotoGIMP.zip)**
4. Extraia o conteúdo de `PhotoGIMP.zip` para qualquer pasta (ex.: sua Área de Trabalho).
5. Abra a pasta extraída e **copie a pasta `3.0`**.
6. Abra o Finder, pressione <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> para abrir "Ir para a Pasta".
7. Digite `~/Library/Application Support/GIMP` e pressione <kbd>Enter</kbd>.
8. Se você tiver uma pasta `2.10` de uma instalação anterior, **exclua-a** para evitar conflitos.
9. **Cole** a pasta `3.0` dentro da pasta do GIMP.
10. Quando perguntado sobre arquivos existentes, selecione **"Substituir"** ou **"Mesclar"**.
11. Abra o GIMP — você deverá ver o novo layout do PhotoGIMP! 🎉

---

## 📦 O Que Está Incluído no Patch

O PhotoGIMP substitui ou adiciona os seguintes arquivos no diretório de configuração do GIMP:

| Arquivo / Pasta | O que faz |
|---|---|
| `shortcutsrc` | Atalhos de teclado mapeados para corresponder ao Photoshop |
| `toolrc` | Configuração e ordenação de ferramentas |
| `sessionrc` | Layout de janelas e posições de painéis |
| `dockrc` | Configuração de painéis / docks |
| `gimprc` | Preferências gerais do GIMP (canvas, grade, etc.) |
| `contextrc` | Configurações de ferramenta/cor ativas |
| `splashes/` | Tela inicial personalizada do PhotoGIMP |
| `theme.css` | Pequenos ajustes no tema da interface |
| `templaterc` | Modelos de canvas pré-definidos |

No Linux, o patch também instala:
- Um arquivo `.desktop` personalizado (lançador com nome e ícone do PhotoGIMP)
- Um ícone personalizado em `~/.local/share/icons/`

---

## 🗑 Como Desinstalar

Para remover o PhotoGIMP e restaurar o GIMP ao estado padrão, basta excluir a pasta de configuração do GIMP e reabri-lo — ele irá regenerar as configurações padrão.

### Linux

```bash
rm -rf ~/.config/GIMP/3.0
```

Depois abra o GIMP novamente — ele criará uma nova configuração padrão.

Se você fez um backup anteriormente, restaure-o:

```bash
cp -r ~/GIMP-3.0-backup ~/.config/GIMP/3.0
```

### Windows

1. Pressione <kbd>Windows</kbd> + <kbd>R</kbd>, digite `%APPDATA%\GIMP` e pressione <kbd>Enter</kbd>.
2. Exclua a pasta `3.0`.
3. Abra o GIMP — ele irá recriar as configurações padrão.

Ou restaure seu backup colando a pasta `3.0` de volta.

### macOS

1. Abra o Finder, pressione <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd>.
2. Vá para `~/Library/Application Support/GIMP`.
3. Exclua a pasta `3.0`.
4. Abra o GIMP — ele irá recriar as configurações padrão.

Ou restaure seu backup colando a pasta de volta.

---

## ❓ Solução de Problemas / FAQ

<details>
<summary><strong>O PhotoGIMP não mudou nada — o GIMP está igual</strong></summary>

- Certifique-se de que você extraiu os arquivos no **local correto**. O erro mais comum é extrair na pasta errada.
- **Linux**: As pastas `.config` e `.local` devem estar no seu diretório pessoal (`~`). Elas são ocultas — pressione <kbd>Ctrl</kbd> + <kbd>H</kbd> no seu gerenciador de arquivos para vê-las.
- **Windows**: A pasta `3.0` deve estar **dentro** de `%APPDATA%\GIMP`, não ao lado dela.
- **macOS**: A pasta `3.0` deve estar **dentro** de `~/Library/Application Support/GIMP`.
- Você **fechou o GIMP** antes de colar os arquivos? O GIMP pode sobrescrever as configurações recebidas ao sair.
</details>

<details>
<summary><strong>Recebo um erro ao abrir o GIMP depois de instalar o PhotoGIMP</strong></summary>

- Isso geralmente significa que a versão do GIMP não corresponde. O PhotoGIMP é feito para o **GIMP 3.0+**. Se você está usando o GIMP 2.x, não será compatível.
- Tente excluir a pasta de configuração e reinstalar — veja a seção [Como Desinstalar](#-como-desinstalar).
</details>

<details>
<summary><strong>Posso usar o PhotoGIMP com o GIMP 2.10?</strong></summary>

Não. Esta versão do PhotoGIMP foi projetada exclusivamente para o **GIMP 3.0 e mais recente**. O formato de configuração mudou significativamente entre o GIMP 2.x e 3.x.
</details>

<details>
<summary><strong>O PhotoGIMP vai apagar meus pincéis, fontes ou plug-ins personalizados?</strong></summary>

Não. O PhotoGIMP substitui apenas arquivos de configuração (atalhos, layout, preferências). Seus pincéis, fontes, gradientes e plug-ins pessoais permanecem intocados.
</details>

<details>
<summary><strong>Posso personalizar os atalhos depois de instalar o PhotoGIMP?</strong></summary>

Com certeza! O PhotoGIMP apenas define um ponto de partida. Você pode alterar qualquer atalho no GIMP em **Editar → Atalhos de Teclado**.
</details>

<details>
<summary><strong>Como atualizo o PhotoGIMP para uma nova versão?</strong></summary>

Basta baixar a versão mais recente e seguir os passos de instalação novamente — isso sobrescreverá a configuração anterior do PhotoGIMP.
</details>

---

## 🤝 Contribuindo

Encontrou um bug? Tem uma sugestão? Adoraríamos sua ajuda!

- **Relatar um problema**: [Abrir uma issue](https://github.com/Diolinux/PhotoGIMP/issues)
- **Enviar uma correção**: [Criar um pull request](https://github.com/Diolinux/PhotoGIMP/pulls)
- **Traduzir**: Ajude-nos a traduzir o README para mais idiomas! Veja a seção [Traduções](#-traduções).

---

## 🌍 Traduções

Este README está disponível em outros idiomas:

- 🇬🇧 [English (Inglês)](../README.md)
- 🇵🇱 [Polski (Polonês)](./README_pl.md)

Quer adicionar seu idioma? Faça um fork do repositório, crie um arquivo `docs/README_xx.md` e envie um pull request!

---

## 🏆 Créditos

- Este projeto não seria possível sem a incrível equipe do [GIMP](https://www.gimp.org/).
- Um GRANDE obrigado a todos os apoiadores do Diolinux no [YouTube](https://youtube.com/Diolinux).
- Tela inicial e ícones de [Adriel Filipe Design](https://bento.me/adrielfilipedesign).

---

## 👥 Contribuidores

<a align="center" href="https://github.com/Diolinux/PhotoGIMP/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Diolinux/PhotoGIMP" />
</a>

---

## 📄 Licença

PhotoGIMP é licenciado sob a [GNU General Public License v3.0](../LICENSE).
