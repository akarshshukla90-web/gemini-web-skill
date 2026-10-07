import argparse
import sys
from src.gemini_web_bridge import GeminiWebBridge

def main():
    parser = argparse.ArgumentParser(
        description="Gemini Web Bridge CLI - Query Google Gemini Pro web via Chrome CDP"
    )
    parser.add_argument(
        "--prompt", "-p", required=True, help="Prompt text to send to Gemini Web"
    )
    parser.add_argument(
        "--cdp-url", default="http://127.0.0.1:9222", help="CDP endpoint URL (default: http://127.0.0.1:9222)"
    )
    parser.add_argument(
        "--timeout", type=int, default=60, help="Response timeout in seconds (default: 60)"
    )

    args = parser.parse_args()

    bridge = GeminiWebBridge(cdp_url=args.cdp_url)

    if not bridge.is_cdp_ready():
        print(f"Error: Chrome CDP is not active at {args.cdp_url}.")
        print("Please start Chrome with '--remote-debugging-port=9222'.")
        sys.exit(1)

    print(f"Sending prompt to Gemini Web...")
    try:
        response = bridge.ask_gemini(args.prompt, timeout=args.timeout)
        print("\n--- Gemini Response ---")
        print(response)
        print("----------------------")
    except Exception as e:
        print(f"Error during Gemini interaction: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
