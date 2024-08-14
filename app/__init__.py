from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.home import home_bp
    from app.routes.customer_routes import customer_bp
    from app.routes.device_type_routes import device_bp
    from app.routes.customer_devices_routes import customer_devices_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(device_bp)
    app.register_blueprint(customer_devices_bp)

    return app
