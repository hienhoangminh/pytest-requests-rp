import requests
import pytest
import json
from assertpy import assert_that
from config import GRAPHQL_URL, TOKEN
import logging

LOGGER = logging.getLogger(__name__)

headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}',
        'Accept': 'application/json'
}

payload = json.dumps({
  "query": "query{users {pageInfo {endCursor startCursor hasNextPage hasPreviousPage} totalCount nodes {id name email gender status}}}"
})

def get_all_users():
    response = requests.post(url=GRAPHQL_URL, data=payload,headers=headers)
    users = response.json()
    return response, users

def test_read_all_list_not_empty():
    LOGGER.info(json.dumps(headers))
    response, users = get_all_users()
    # users = response.json()
    
    # assert_that(response.status_code).is_equal_to(200)
    # user_names = [user['name'] for user in users]
    # assert_that(users).extracting('name').is_not_empty()
    logging.info(json.loads(response.text))