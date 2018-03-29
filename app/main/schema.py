from marshmallow import Schema, fields


class TechnologySchema(Schema):
    id = fields.Integer()
    name = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class CompanySchema(Schema):
    id = fields.Integer()
    email = fields.Email()
    name = fields.String()
    web_site = fields.String()
    has_github = fields.Boolean()
    technologies = fields.Nested(TechnologySchema, many=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
