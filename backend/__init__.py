from flask import Flask
from config import Config
from flask_cors import CORS

# db = SQLAlchemy()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions here
    # db.init_app(app)
    cors.init_app(app)

    # Add blueprints here
    from corona.routes import corona
    app.register_blueprint(corona)

    # inorder to use this app at different places, use current app
    # from flask import current_app
    return app