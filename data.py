from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("not found")
else:
    print("Token found")
