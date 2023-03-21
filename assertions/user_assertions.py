from assertpy import assert_that, soft_assertions

class UserAssertions:
    def assert_status_code(expected_code, actual_code):
        assert_that(expected_code).is_equal_to(actual_code)
    
    def assert_users_not_empty(response):
        assert_that(response.as_dict).is_not_empty()
        
    def assert_user_id_correct(expectedId, actualId):
        assert_that(expectedId).is_equal_to(actualId)
    
    def assert_created_user_correct(expected_name, actual_name):
        assert_that(expected_name).is_equal_to(actual_name)
        
    def assert_user_with_name_found(expected_dict, name):
        is_new_user_created = filter(lambda user: user['name'] == name, expected_dict)
        assert_that(is_new_user_created).is_true()
