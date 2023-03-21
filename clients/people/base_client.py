from config import TOKEN

class BaseClient:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}'
        }