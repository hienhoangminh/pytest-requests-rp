import json
import requests
from assertpy import assert_that, soft_assertions
from config import BASE_URL, TOKEN
from cerberus import Validator
from clients.people.user_client import UserClient
from assertions.user_assertions import UserAssertions
import logging

userClient = UserClient()
logger = logging.getLogger(__name__)

schema = {
    "id": { 'type' : 'number'},
    "name": { 'type': 'string'},
    "email": { 'type': 'string'},
    "gender": { 'type': 'string'},
    "status": { 'type': 'string'}
}

def test_read_one_user_has_expected_schema():
    # logger.debug("Invoking API POST /v2/users...")
    id = userClient.get_random_user_id_from_list()
    response = userClient.get_user_by_id(id)
      
    logger.debug(f'Status : {response.status_code}')
    logger.debug(f'Response: {response.as_dict}')

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(response.as_dict)
    assert_that(is_valid, description=validator.errors).is_true()
    
def test_read_all_user_has_expected_schema():
    response = userClient.get_all_user()
    
    logger.debug(f'Status : {response.status_code}')
    logger.debug(f'Response: {response.as_dict}')

    
    validator = Validator(schema, require_all=True)
    with soft_assertions():
        for user in response.as_dict:
            is_valid = validator.validate(user)
            assert_that(is_valid, description=validator.errors).is_true()    