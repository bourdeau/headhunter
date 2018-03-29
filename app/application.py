from flask import Flask, jsonify
from flask_security import SQLAlchemyUserDatastore
from importlib import import_module
from app.blueprints import all_blueprints
from app.extensions import db, migrate, security, ma, cors
# Must be after db because classes need db
from app.main.models import User, Role
from app.commands import init_db, scrap_wtj, scrap_github


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role))

    return None


def register_blueprints(app):

    # There is only one module
    import_module(all_blueprints.import_name)
    app.register_blueprint(all_blueprints)

    # for module in all_blueprints:
    #     import_module(module.import_name)
    #     app.register_blueprint(module)

    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': User
        }

    app.shell_context_processor(shell_context)


def register_commands(app):
    """ Register Commands """
    app.cli.add_command(init_db)
    app.cli.add_command(scrap_wtj)
    app.cli.add_command(scrap_github)


def register_errorhandlers(app):
    @app.errorhandler(404)
    def not_found_404(error):
        return jsonify(error=404, text=str(error)), 404

    @app.errorhandler(500)
    def not_found_500(error):
        return jsonify(error=500, text=str(error)), 500
