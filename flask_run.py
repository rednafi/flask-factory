from app import create_app
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

application = create_app()

# Uncomment this while testing the app locally
if os.environ.get("RUNTIME_ENVIRONMENT").lower() == "development":
    application.run(host="0.0.0.0", port=5000, debug=True)
