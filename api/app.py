from flask import Flask
from api.api_config import get_config
from flask_restx import Api
from api.models import create_models
from api.endpoints.routes import register_routes

def create_app():
    config = get_config()

    app = Flask(__name__)
    api = Api(app,
              version=config.API_VERSION,
              title=config.API_TITLE,
              description=config.API_DESCRIPTION,
              doc=config.API_DOC_PATH,
              ui = True)

    # Create Swagger models
    models = create_models(api)

    # Register Routes
    register_routes(api, models)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
