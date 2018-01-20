HeadHunter
============

Okay to make it simple I'm looking for a job but as I'm very lazy to manually
look for companies, technologies that fit my skills, contact etc. I decided to
code a little bit to help me scrap the web for this kind of informations 😈

## Installation
```bash
pipenv install
```

## Install db
```bash
pipenv shell
export FLASK_APP=run.py

flask init_db
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
