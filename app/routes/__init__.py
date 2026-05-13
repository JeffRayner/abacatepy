from flask import render_template, flash
from app.routes.home import home_bp


def registrer_routes(app):

    @app.errorhandler(Exception)
    def handle_not_found(_exc):
        code = getattr(_exc, 'code', 500)
        flash("Page not found", "danger")
        return render_template("error.html"), code
    
    blueprint_routes = [home_bp]
    for route in blueprint_routes:
        app.register_blueprint(route)
