import pytest
from faker import Faker
from utils.file_reader import read_file
import random
import logging
import sys
from reportportal_client import RPLogger

faker = Faker()

@pytest.fixture
def create_data():
    payload = read_file('create_person.json')
    first_name = faker.name()
    gender = random.choice(['male', 'female'])
    email = faker.email()
    
    payload['name'] = first_name
    payload['gender'] = gender
    payload['email'] = email
    
    yield payload

# @pytest.fixture(scope="session")
# def logger(request):
#    logger = logging.getLogger(__name__)
#    logger.setLevel(logging.DEBUG)

#    # Create a handler for Report Portal if the service has been
#    # configured and started.
#    if hasattr(request.node.config, 'py_test_service'):
#        # Import Report Portal logger and handler to the test module.
#        logging.setLoggerClass(RPLogger)
#        rp_handler = RPLogHandler(request.node.config.py_test_service)

#        # Add additional handlers if it is necessary
#        console_handler = logging.StreamHandler(sys.stdout)
#        console_handler.setLevel(logging.INFO)
#        logger.addHandler(console_handler)
#    else:
#        rp_handler = logging.StreamHandler(sys.stdout)

#    # Set INFO level for Report Portal handler.
#    rp_handler.setLevel(logging.INFO)
#    return logger


def pytest_addoption(parser):
    # Method to add the option to ini
    parser.addini("rp_uuid",'help',type="pathlist")
    parser.addini("rp_endpoint",'help',type="pathlist")
    parser.addini("rp_project",'help',type="pathlist")
    parser.addini("rp_launch",'help',type="pathlist")              
 
@pytest.hookimpl()
def pytest_configure(config):
    # Sets the launch name based on the marker selected.
    suite = config.getoption("markexpr")
    try:
        config._inicache["rp_uuid"]="18737aa8-d339-4521-9c3f-73e6fff3b249"
        config._inicache["rp_endpoint"]="http://localhost:8080"
        config._inicache["rp_project"]="gorest_user_api"
        config._inicache["rp_launch"]="gorest_user_api"
 
    except Exception as e:
        print (str(e))