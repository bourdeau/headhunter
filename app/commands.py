import click
from sqlalchemy_utils import database_exists, create_database
from flask import current_app
from flask.cli import with_appcontext
from app.application import db
from app.main.models import User
from app.scrapers.wtj.wtj import Wtj
from app.scrapers.github.scraper import GithubScraper


@click.command()
@with_appcontext
def init_db():
    """ Initialize db """
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_uri):
        create_database(db_uri)
    else:
        db.drop_all()

    db.create_all()

    # Fixtures
    user = User()
    user.email = 'phbasic@gmail.com'
    user.password = '123456789'
    user.active = True
    db.session.add(user)
    db.session.commit()

    print('Initialized the database.')


@click.command()
@with_appcontext
def scrap_wtj():
    """Scrap Welcome To The Jungle"""
    wtj = Wtj()
    wtj.run()


@click.command()
@with_appcontext
def scrap_github():
    """ Scrap Github"""
    github = GithubScraper(current_app.config['GITHUB_EMAIL'], current_app.config['GITHUB_PASSWORD'])
    github.run()
