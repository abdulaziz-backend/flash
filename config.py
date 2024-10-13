import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "7862006989:AAGoj1rYfPgu65JzlwtYYhOHucScw2_ueeg"
OWNER_ID = 6236467772
REQUIRED_CHANNEL = "@pythonnews_uzbekistan"
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://flashdownloader_user:8D8kPH52tEsZHPCyxGxTSKt8lQuSszMz@dpg-cs5vejt6l47c73f8ta9g-a.oregon-postgres.render.com/flashdownloader')