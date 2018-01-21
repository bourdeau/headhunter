HeadHunter
============

Okay to make it simple I'm looking for a job but as I'm very lazy to manually
look for companies, technologies that fit my skills, contact etc. I decided to
code a little bit to help me scrap the web for this kind of informations 😈

## Installation
```bash
pipenv install

cp config-dist.py config.py
# Edit config.py for you needs
```

## Install db and run scraping
```bash
pipenv shell
export FLASK_APP=run.py

# Create a fresh database
flask init_db

# Create comapnies from WTJ
flask scrap_wtj

# Get contact info from Github
flask scrap_github
```

## Run
```bash
pipenv shell
export FLASK_APP=run.py
export FLASK_DEBUG=1

flask run
```

## Migrations:
```bash
pipenv shell
export FLASK_APP=run.py

flask db migrate
flask db upgrade
```
