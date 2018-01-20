import datetime
from flask_security import UserMixin, RoleMixin
from app.application import db

roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey(
    'user.id')), db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


company_tech = db.Table('company_technology', db.Model.metadata,
                        db.Column('company_id', db.Integer,
                                  db.ForeignKey('company.id')),
                        db.Column('technology_id', db.Integer,
                                  db.ForeignKey('technology.id'))
                        )


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    web_site = db.Column(db.UnicodeText(), unique=False)
    has_github = db.Column(db.Boolean, unique=False, default=False)
    email = db.Column(db.String(255), unique=True)
    technologies = db.relationship('Technology', secondary=company_tech)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False)

    def __repr__(self):
        return '<Company %r>' % self.name

    @classmethod
    def __declare_last__(cls):
        db.event.listen(cls, 'before_update', cls._before_update)

    @staticmethod
    def _before_update(mapper, connection, target):
        target.updated_at = datetime.datetime.now()


class Technology(db.Model):
    __tablename__ = 'technology'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False)

    def __repr__(self):
        return '<Technology %r>' % self.name

    @classmethod
    def __declare_last__(cls):
        db.event.listen(cls, 'before_update', cls._before_update)

    @staticmethod
    def _before_update(mapper, connection, target):
        target.updated_at = datetime.datetime.now()
