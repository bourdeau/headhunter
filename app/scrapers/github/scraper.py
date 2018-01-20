from github import Github
from app.main.models import Company
from urllib.parse import urlparse
from email_split import email_split
from app.application import db


class GithubScraper():

    def __init__(self, email, password):
        self.github = Github(email, password)

    def run(self):

        companies = Company.query.all()

        for company in companies:
            results = self.github.search_users(query=company.name)
            nb = results.totalCount

            if nb == 0:
                continue

            self.get_company_data(company, results)

    def get_company_data(self, company, results):

            limit = 10
            index = 0
            for user in results:
                if index == limit:
                    break

                if not user.blog and not user.email:
                    continue

                company_domain = urlparse(company.web_site).netloc

                if user.blog:
                    user_domain = urlparse(user.blog).netloc

                # Blog domain is preffered over email
                if user.email and not user.blog:
                    email = email_split(user.email)
                    user_domain = email.domain

                if company_domain == user_domain:
                    company.has_github = True
                    if user.email:
                        company.email = user.email

                    db.session.add(company)
                    db.session.commit()
                    # self.get_users(user)

                index += 1

    def get_users(self, user):
        """Unused for now"""
        print("==> Nb orgs: {}".format(user.get_orgs().totalCount))

        for org in user.get_orgs():
            print('Membeeeeeee')
            members = org.get_members()

            for member in members:
                print("What the fuck: {}".format(member.name))
