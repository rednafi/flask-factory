from pathlib import Path

from konfik import Konfik

# Env file directory
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ENV_FILE = BASE_DIR / ".env"

# Read .env
konfik = Konfik(ENV_FILE)
config = konfik.config
