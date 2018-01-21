import urllib
from urllib.parse import urlparse
from .client import Client
from bs4 import BeautifulSoup
from app.main.models import Company, Technology
from app.application import db


class Wtj():
    """ Welcome To The Jungle Scraper"""

    def __init__(self):
        self.base_url = 'https://www.welcometothejungle.co'

    def run(self):
        for page in range(0, 30):
            if page == 0:
                page_html = self._get_page_html('/stacks')
            else:
                page_html = self._get_page_html('/stacks', {'p': page})

            self._get_company_block(page_html)

    def _get_page_html(self, route, params=None):
        client = Client()

        url = self.base_url + route

        if params:
            url = url + '?' + urllib.parse.urlencode(params)

        html = client.request(url)

        return BeautifulSoup(html, 'lxml')

    def _get_company_block(self, soup: BeautifulSoup):
        """
        Get data from Block company
        """

        for company_block in soup.find_all("article", {"class": "company-item with-stack"}):
            company = {}
            company['title'] = company_block.find("h4", {"class": "company-name"}).contents[0].strip()
            url = company_block.find("a", {"class": "company-link"}).get('href')
            page_data = self._get_company_page(url)
            company['city'] = page_data['city']

            uri = urlparse(page_data['website'])
            company['website'] = "{}://{}".format(uri.scheme, uri.netloc)

            span_subtitle = company_block.find("p", {"class": "company-subtitle"})
            company['activity'] = span_subtitle.find("span").text.strip()

            stacks = []
            for stack in company_block.find_all("span", {"class": "stack-label"}):
                stacks.append(stack.contents[0].strip())

            company['stack'] = stacks

            self._save(company)

    def _save(self, company_dict: BeautifulSoup):

        company = Company.query.filter_by(name=company_dict['title']).first()

        if not company:
            company = Company()

        company.name = company_dict['title']
        company.web_site = company_dict['website']

        for stack in company_dict['stack']:
            technology = Technology.query.filter_by(name=stack).first()
            if not technology:
                technology = Technology()
                technology.name = stack
            company.technologies.append(technology)

        db.session.add(company)
        db.session.commit()

    def _get_company_page(self, url):
        page_html = self._get_page_html(url)

        meta = page_html.find("ul", {"class": "page-metas"})

        city = meta.find_all('span')[1].text

        website_url = None

        if meta.find_all('a'):
            website_url = meta.find_all('a')[0].get('href')

        return {'city': city, 'website': website_url}
