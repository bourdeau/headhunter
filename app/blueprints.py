from flask import Blueprint

main = Blueprint('main', 'app.main.controllers', template_folder='templates')

all_blueprints = (main)
