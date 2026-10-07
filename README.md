# Gemini Web Skill & CDP Bridge for Hermes Agent

> **Zero API Costs:** Leverage your existing Google Gemini Pro / Gemini Advanced web subscription via browser CDP automation in Hermes Agent and CLI.

---

## 📌 Overview

`gemini-web-skill` connects **Hermes Agent** (and standalone CLI applications) directly to **Google Gemini** (`https://gemini.google.com`) through your local logged-in Chrome profile via **Chrome DevTools Protocol (CDP)**.

Instead of paying per-token API fees for `gemini-1.5-pro` / `gemini-2.0`, this tool routes prompt queries directly through your active browser session where your Gemini Advanced / Google One AI Premium subscription is already active.

---

## ✨ Features

- **Profile Reuse**: Attaches to your existing logged-in Chrome profile (no re-login or 2FA bypass needed).
- **Hermes Skill Ready**: Native `SKILL.md` included for seamless integration into Hermes Agent workflows.
- **CDP Automation**: Fast, reliable Chrome DevTools Protocol control (Playwright / Pyppeteer backend).
- **Cost Savings**: Unlocks unlimited/subscription-based Gemini Pro queries without API token billing.
- **CLI & Python API**: Usable as a standalone terminal command or Python library.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+
- Google Chrome browser logged into Google Gemini (`https://gemini.google.com`)

### 2. Launch Chrome with Remote Debugging Enabled

#### Windows:
```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data" --profile-directory="Profile 9"
```
*(Replace `Profile 9` with your logged-in profile directory, e.g., `Default` or `Profile 1`)*

#### macOS:
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="$HOME/Library/Application Support/Google/Chrome"
```

#### Linux:
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="$HOME/.config/google-chrome"
```

---

### 3. Installation

```bash
git clone https://github.com/your-username/gemini-web-skill.git
cd gemini-web-skill
pip install -r requirements.txt
```

---

## 🛠️ Usage

### Python CLI
```bash
python -m src.cli --prompt "Explain quantum computing in simple terms"
```

### Hermes Agent Skill Setup
Copy `skills/gemini-web` to your Hermes skills directory:
```bash
cp -r skills/gemini-web ~/.hermes/skills/
```

Inside Hermes:
```
Ask Gemini: "Analyze this document and summarize key findings"
```

---

## 🔒 Security & Privacy

- All browser interactions happen locally on your own machine.
- No credentials or cookies are transmitted outside your local environment.
- Uses standard Chrome CDP over localhost port `9222`.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.
