# pytest-requests-rp

This project showcases how to perform API testing with requests and pytest. Report chosen is ReportPortal.

Pre-requisites:
- Have Python installed
- Installed pipenv with _pip install pipenv_
- Run _pipenv install_ to install all dependencies
- Run _pipenv shell_ to activate pipenv
- Either you can choose to create new directory with _mkdir -p data/elasticsearch_ or use the existing data directory 
- Give permission to this directory with _chmod 777 data/elasticsearch_
- Finally run this command: _chgrp 1000 data/elasticsearch_
- Run: _docker-compose -p reportportal up -d --force-recreate_ to install all dependencies and bring up to work ReportPortal
- Verified that we can see ReportPortal at http://localhost:8080

Guide:
- Run the tests with: pipenv run pytest ./tests
- Run the tests and push to ReportPortal with: pipenv run pytest ./tests --reportportal
