import requests
from clients.people.user_client import UserClient
from assertions.user_assertions import UserAssertions

userClient = UserClient()

def test_get_all_users():
    """
    Test case to test API GET https://gorest.co.in/public/v2/users
    """
    # logger.debug("Invoking API GET /v2/users...")
    response = userClient.get_all_user()
    # logger.debug(f'Status : {response.status_code}')
    # logger.debug(f'Response: {response.as_dict}')

    UserAssertions.assert_status_code(response.status_code, requests.codes.ok)
    UserAssertions.assert_users_not_empty(response)
    
def test_get_user_by_id():
    """
    Test case to test API GET https://gorest.co.in/public/v2/users/{id}
    """
    # logger.debug("Invoking API GET /v2/users/{id}...")
    id = userClient.get_random_user_id_from_list()
    # logger.debug("User id %s...", id)
    
    response = userClient.get_user_by_id(id)
    # logger.debug(f'Status : {response.status_code}')
    # logger.debug(f'Response: {response.as_dict}')
    
    UserAssertions.assert_status_code(response.status_code, requests.codes.ok)
    UserAssertions.assert_user_id_correct(response.as_dict['id'], id)

def test_new_user_can_be_added():
    """
    Test case to test API POST https://gorest.co.in/public/v2/users
    """
    # logger.debug("Invoking API POST /v2/users...")
    unique_name, response = userClient.create_user()
    
    # logger.debug(f'Status : {response.status_code}')
    # logger.debug(f'Response: {response.as_dict}')
    
    UserAssertions.assert_status_code(response.status_code, requests.codes.created)
    UserAssertions.assert_created_user_correct(response.as_dict["name"], unique_name)
    
def test_user_can_be_updated():
    """
    Test case to test API PATCH https://gorest.co.in/public/v2/users/{id}
    """
    # logger.debug("Invoking API PUT /v2/users/{user_id}...")
    _, user_id = userClient.get_user_name_and_id_of_created_user()
    
    unique_name, response = userClient.update_user_by_id(user_id)
    
    # logger.debug(f'Status : {response.status_code}')
    # logger.debug(f'Response: {response.as_dict}')
    
    UserAssertions.assert_status_code(response.status_code, requests.codes.ok)
    
    response = userClient.get_all_user()
    UserAssertions.assert_user_with_name_found(response.as_dict, unique_name)
    
    
def test_user_can_be_deleted():
    """
    Test case to test API DELETE https://gorest.co.in/public/v2/users/{id}
    """
    # logger.debug("Invoking API DELETE /v2/users/{user_id}...")
    _, user_id = userClient.get_user_name_and_id_of_created_user()

    response = userClient.delete_user(user_id)
    # logger.debug(f'Status : {response.status_code}')
    # logger.debug(f'Response: {response.as_dict}')
    UserAssertions.assert_status_code(response.status_code, requests.codes.no_content)
    
    response = userClient.get_user_by_id(user_id)
    UserAssertions.assert_status_code(response.status_code, requests.codes.not_found)
    
def test_user_can_be_added_with_json_template(create_data):
    # logger.info('API POST /v2/users with payload came from file')
    unique_name, response = userClient.create_user(create_data)
    
    # logger.debug(f'Status : {response.status_code}')
    # logger.debug(f'Response: {response.as_dict}')
    
    UserAssertions.assert_status_code(response.status_code, requests.codes.created)
    UserAssertions.assert_created_user_correct(response.as_dict["name"], unique_name)   
        