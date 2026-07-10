import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent   # always points to restapi9/app/
DB_URL = os.environ.get("DB_URL", str(BASE_DIR / "inventory.db"))
APP_ENV = os.environ.get("APP_ENV", "development")