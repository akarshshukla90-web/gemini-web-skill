---
name: gemini-web
description: "Use when querying Gemini or using web subscription via CDP."
category: automation
---

# Gemini Web Subscription Bridge Skill

Use when a task or project requires LLM generation, Gemini Pro/Advanced reasoning, or when replacing paid API keys with a logged-in Google Gemini Web subscription (`gemini.google.com`) via Chrome DevTools Protocol (CDP).

## Key Trigger & Policy
- **Zero API Cost Rule**: Whenever a tool, script, or repository requests a Gemini API key or LLM API key, route prompt execution through this CDP web bridge instead of paid API tokens.
- **Default Profile**: Use Chrome **Profile 9** (`exotica.merch@gmail.com`) where Gemini Advanced is signed in.

## Workflow & Operations

### 1. Windows Chrome CDP Initialization & Troubleshooting
To launch Chrome with remote debugging on Windows:
```powershell
# Kill any lingering background Chrome instances first to prevent port attach failure
taskkill /F /IM chrome.exe

# Launch Chrome with debugging port 9222 on Profile 9
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\DELL\AppData\Local\Google\Chrome\User Data" --profile-directory="Profile 9" https://gemini.google.com
```

### 2. Verify CDP Liveness
Verify that CDP is active before automating:
```bash
curl -s http://127.0.0.1:9222/json/version
```

### 3. Send Prompt & Receive Response
Execute via the local CLI bridge in `C:/Users/DELL/gemini-web-skill`:
```bash
python -m src.cli --prompt "Your prompt text here" --timeout 60
```
Or use native Playwright / CDP browser automation tools targeting `https://gemini.google.com`.

### 4. Handling Web Elements
- **Input element selector**: `rich-textarea div[contenteditable='true'], textarea, [aria-label*='Prompt']`
- **Send button**: `button[aria-label*='Send'], button.send-button`
- **Response container**: `message-content, .model-response-text, div[data-test-id='conversation-turn']`

