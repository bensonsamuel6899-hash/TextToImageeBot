import os

# Try multiple possible variable names
TOKEN = os.environ.get("TELEGRAM_TOKEN") or os.environ.get("BOT_TOKEN") or os.environ.get("TOKEN")

# Debug: Print first few characters to verify it's loaded
if TOKEN:
    print(f"Token loaded: {TOKEN[:10]}...")
else:
    print("ERROR: No token found in environment variables!")
    print("Available variables:", list(os.environ.keys()))
    exit(1)
