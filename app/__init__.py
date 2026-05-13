from os import getenv
from flask import Flask


def create_app():
    app = Flask( __name__, instance_relative_config=True,
        template_folder="templates", static_folder="static",
    )

    from app.routes import registrer_routes

    with app.app_context():
        app.config["SECRET_KEY"] = getenv("SECRET_KEY", "")
        registrer_routes(app)

    return app
