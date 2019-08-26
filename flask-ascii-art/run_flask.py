import os
from app import create_app

# environment = os.environ.get("ENVIRONMENT", "PRODUCTION")
environment = "DEVELOPMENT"
application = create_app()
if environment != "PRODUCTION":
    if __name__ == "__main__":
        application.run(host="0.0.0.0", port=5000, debug=True)
