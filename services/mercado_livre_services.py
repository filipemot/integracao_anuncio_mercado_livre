from typing import Optional, Any

import requests

from services.config_services import ConfigServices


class MercadoLivreServices:
    def __init__(self):
        self.config_services = ConfigServices()

    def save_pictures(self, name: str, path: str, extension: str) -> Optional[Any]:
        url = f"{self.config_services.mercado_livre_api_url}/pictures/items/upload"

        files = {'file': (name, open(path, 'rb'), extension)}

        headers = {
            'Authorization': 'BEARER ' + self.config_services.token
        }

        response = requests.request("POST", url, headers=headers, files=files)

        if response.status_code == 201:
            return response.json()['id']
        else:
            return None
