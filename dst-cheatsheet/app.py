from flask import Flask

def create_app():
    app = Flask(__name__)

    # Enable automatic template reloading
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Import and register the views
    from views import views_blueprint
    app.register_blueprint(views_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
