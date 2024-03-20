import requests

class StarWarsApi:
    def __init__(self):
        self.base_url = 'https://swapi.dev'

    def get_entity(self, entity, entity_id):
        url = f"{self.base_url}/api/{entity}/{entity_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f'Неможливо отримати дані у сутності {entity} з ідентифікатором {entity_id}')
