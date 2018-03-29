from app.blueprints import main
from flask import request
from app.main.models import Company
from app.main.schema import CompanySchema
from flask import jsonify


@main.route("/companies", methods=['GET'])
def get_companies():
    nb_record = 20
    p = request.args.get('p')

    page = int(p) if p else 1

    companies = Company.query.paginate(page, nb_record, False)
    total = companies.total
    companies_schema = CompanySchema(many=True)
    result = companies_schema.dump(companies.items)

    data = {
        "total": total,
        "data": result.data
    }

    return jsonify(data)


@main.route("/companies/<id>", methods=['GET'])
def get_company(id):

    company = Company.query.get(id)
    companies_schema = CompanySchema()
    result = companies_schema.dump(company)

    return jsonify(result)
