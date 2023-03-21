from json import dumps
from uuid import uuid4
from clients.people.base_client import BaseClient
from config import BASE_URL
from utils.request import APIRequest
from faker import Faker
import random
import logging

LOGGER = logging.getLogger(__name__)

class UserClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URL
        self.request = APIRequest()
        self.faker = Faker()
        
    def create_user(self, body=None):
        unique_name, response = self.__create_user_with_unique_name(body)
        return unique_name, response
    
    def __create_user_with_unique_name(self, body=None):
        if body is None:
            unique_name = self.faker.name()
            payload = dumps({
                'name': unique_name,
                'gender': random.choice(['male', 'female']),
                'email': self.faker.email(),
                'status': 'active'
            })
        else:
            unique_name = body['name']
            payload = dumps(body)
        logging.debug(f'Request payload: {body}')    
        response = self.request.post(self.base_url + "/users", payload, self.headers)
        return unique_name, response
    
    def __update_user_with_unique_name(self, id, body=None):
        if body is None:
            unique_name = f'User {str(uuid4())}'
            payload = dumps({
                'name': unique_name,
                'gender': random.choice(['male', 'female']),
                'email': self.faker.email(),
                'status': 'active'
            })
        else:
            unique_name = body['name']
            payload = dumps(body)
        logging.debug(f'Request payload: {body}')    
        response = self.request.patch(f'{self.base_url}/users/{id}', payload, self.headers)
        return unique_name, response
    
    def get_all_user(self):
        return self.request.get(self.base_url + "/users", self.headers)
    
    def get_random_user_id_from_list(self):
        response = self.get_all_user()
        return random.choice(response.as_dict)['id']
        
    def get_user_name_and_id_of_created_user(self):
        name, response = self.create_user()
        return name, response.as_dict['id']
    
    def get_user_by_id(self, id):
        return self.request.get(f'{self.base_url}/users/{id}', self.headers)
    
    def update_user_by_id(self, id, body=None):
        unique_name, response = self.__update_user_with_unique_name(id, body)
        return unique_name, response

    def delete_user(self, user_id):
        url = f'{BASE_URL}/users/{user_id}'
        return self.request.delete(url, self.headers)
                