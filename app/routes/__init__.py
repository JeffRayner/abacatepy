from flask import render_template, flash
from app.routes.home import home_bp
from app.routes.hook import payment_bp

def registrer_routes(app):

    @app.errorhandler(Exception)
    def handle_not_found(_exc):
        code = getattr(_exc, 'code', 500)
        flash("Page not found", "danger")
        print(f'ERRO GERAL: {_exc}')
        return render_template("404.html"), code
    
    @app.context_processor
    def inject_auth_context():
        # função para injetar variaveis nos templates
        return {
            "CURRENT_YEAR": 2026,
            "SITE_NAME": "Abacate Pay",
            "SOCIAL_LINKS": [
                ('Instagram','#'),
                ('Facebook','#'),
                ('Twitter-x', '#')
            ]
        }


    @app.before_request
    def load_request_user():
        # Implementar metodo para pegar 
        # usuario que esta acessando
        pass


    @app.after_request
    def apply_security_headers(response):
        """Apply lightweight hardening headers and avoid caching authenticated HTML."""
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "same-origin")

        return response
    

    blueprint_routes = [home_bp, payment_bp]
    for route in blueprint_routes:
        app.register_blueprint(route)
    

