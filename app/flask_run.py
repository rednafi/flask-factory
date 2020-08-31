from . import create_app
from . import settings

application = create_app()

if settings.ENVIRONMENT == "development":
    application.run(host=settings.HOST, port=settings.PORT, debug=True)
