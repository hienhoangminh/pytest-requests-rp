# pytest-requests-rp

This project showcases how to perform API testing with requests and pytest. Report chosen is ReportPortal.

Pre-requisites:
- Have Python installed
- Installed pipenv with pip install pipenv
- Run pipenv install to install all dependencies
- Run pipenv shell to activate pipenv
- Run: docker-compose -p reportportal up -d --force-recreate to install all dependencies and bring up to work ReportPortal
- Verified that we can see ReportPortal at http://localhost:8080

Guide:
- Run the tests with: pipenv run pytest ./tests
- Run the tests and push to ReportPortal with: pipenv run pytest ./tests --reportportal
