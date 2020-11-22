from . import create_app
from .settings import config

application = create_app()

if config.ENVIRONMENT == "development":
    application.run(host=config.HOST, port=config.PORT, debug=True)
