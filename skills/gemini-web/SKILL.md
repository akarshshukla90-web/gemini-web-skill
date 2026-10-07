---
name: gemini-web
description: Route prompt queries through Google Gemini Web subscription using Chrome CDP to save API token costs.
category: automation
---

# Gemini Web Subscription Bridge Skill

Use this skill when the user asks to send prompts, generate content, or run tasks through their logged-in Google Gemini Pro / Advanced web subscription (`gemini.google.com`) using browser CDP automation.

## Workflow

1. **Check CDP Endpoint Liveness**
   Verify port `9222` on `http://127.0.0.1:9222/json/version`.
   If CDP is not active, instruct the user or execute command to launch Chrome with `--remote-debugging-port=9222`.

2. **Connect via Browser CDP**
   Use browser CDP tools or Python bridge script (`python -m src.cli --prompt "..."`) to navigate to `https://gemini.google.com`.

3. **Send Prompt & Extract Response**
   - Type prompt into rich-textarea on Gemini web interface.
   - Click submit or press Enter.
   - Wait for completion / stop-generating indicator.
   - Read and format response text.

4. **Return Results**
   Present response from Gemini to the conversation.
