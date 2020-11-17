from konfik import Konfik
from pathlib import Path

# Env file directory
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ENV_FILE = BASE_DIR / ".env"

# Read .env
konfik = Konfik(ENV_FILE)
config = konfik.config

# Variables
ENVIRONMENT = config.ENVIRONMENT
HOST = config.HOST
PORT = config.PORT
