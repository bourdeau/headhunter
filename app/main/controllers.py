from app.blueprints import main
from flask import render_template, request
from flask_security import login_required
from app.main.models import Company


@main.route("/", methods=['GET'])
@login_required
def home():
    companies = Company.query.all()

    return render_template('home.html', companies=companies)
