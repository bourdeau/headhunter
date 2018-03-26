from app.blueprints import main
from flask import render_template, request
from app.main.models import Company
from app.main.schema import CompanySchema
from flask import jsonify

@main.route("/", methods=['GET'])
def home():
    companies = Company.query.all()
    companies_schema = CompanySchema(many=True)
    result = companies_schema.dump(companies)

    return jsonify(result.data)
