import environ
from pathlib import Path

# Env file directory
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ENV_FILE = BASE_DIR / ".env"

# Variable cast
env = environ.Env(PORT=int)

# Read env file
env.read_env(str(ENV_FILE))

# Variables
ENVIRONMENT=env("ENVIRONMENT")
HOST=env("HOST")
PORT=env("PORT")

