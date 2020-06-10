from flask import Flask
from corona.util import clear_cache_thread
from config import Config
from flask_cors import CORS
from threading import Thread
from flask_mail import Mail

# extensions 
# db = SQLAlchemy()
cors = CORS()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions here
    # db.init_app(app)
    cors.init_app(app)
    mail.init_app(app)

    # Add blueprints here
    from corona.routes import corona
    app.register_blueprint(corona)


    # THREADS HERE
    cache_thread = Thread(target=clear_cache_thread, daemon=True)
    cache_thread.start()

    # inorder to use this app at different places, use current app
    # from flask import current_app
    return app