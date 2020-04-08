from app import create_app
from dynaconf import settings

application = create_app()

# Uncomment this while testing the app locally
if settings.ENVIRONMENT == "development":
    application.run(host="0.0.0.0", port=4000, debug=True)
