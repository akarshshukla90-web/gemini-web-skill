import json
import time
import urllib.request
from typing import Optional
from playwright.sync_api import sync_playwright, Page

DEFAULT_CDP_URL = "http://127.0.0.1:9222"
GEMINI_URL = "https://gemini.google.com"

class GeminiWebBridge:
    def __init__(self, cdp_url: str = DEFAULT_CDP_URL):
        self.cdp_url = cdp_url

    def is_cdp_ready(self) -> bool:
        try:
            req = urllib.request.urlopen(f"{self.cdp_url}/json/version", timeout=3)
            return req.status == 200
        except Exception:
            return False

    def ask_gemini(self, prompt: str, timeout: int = 60) -> str:
        if not self.is_cdp_ready():
            raise RuntimeError(
                f"Chrome CDP not detected on {self.cdp_url}. "
                "Ensure Chrome is running with '--remote-debugging-port=9222'."
            )

        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(self.cdp_url)
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            
            # Look for existing Gemini page or open new tab
            page: Optional[Page] = None
            for p_item in context.pages:
                if "gemini.google.com" in p_item.url:
                    page = p_item
                    break

            if not page:
                page = context.new_page()
                page.goto(GEMINI_URL, wait_until="domcontentloaded")

            page.bring_to_front()

            # Locate input field (rich-textarea / div[contenteditable='true'] / textarea)
            textarea = page.locator("rich-textarea div[contenteditable='true'], textarea, [aria-label*='Prompt']").first
            textarea.wait_for(state="visible", timeout=15000)
            textarea.click()
            textarea.fill(prompt)

            # Click send button or press Enter
            send_btn = page.locator("button[aria-label*='Send'], button.send-button").first
            if send_btn.is_visible():
                send_btn.click()
            else:
                textarea.press("Enter")

            # Wait for generation to complete
            time.sleep(3)
            # Wait for response text element
            response_locator = page.locator("message-content, .model-response-text, div[data-test-id='conversation-turn']").last
            response_locator.wait_for(state="visible", timeout=timeout * 1000)

            # Give a brief moment for streaming text to finalize
            time.sleep(2)
            result_text = response_locator.inner_text()
            return result_text.strip()
