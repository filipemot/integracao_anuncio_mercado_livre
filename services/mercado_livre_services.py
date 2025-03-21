import json
from typing import Optional, Any

import requests


class MercadoLivreServices:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token


    def save_pictures(self, name: str, path: str, extension: str) -> Optional[Any]:
        url = f"{self.url}/pictures/items/upload"

        files = {'file': (name, open(path, 'rb'), extension)}

        headers = {
            'Authorization': 'BEARER ' + self.token
        }

        response = requests.request("POST", url, headers=headers, files=files)

        if response.status_code == 201:
            return response.json()['id']
        else:
            print(response.text)
            return None

    def save_advertisement(self, mercado_livre_advertisement: any) -> Optional[Any]:
        url = f"{self.url}/items"

        payload = json.dumps(mercado_livre_advertisement.to_json(), ensure_ascii=False)

        headers = {
            'Authorization': 'BEARER ' + self.token
        }

        print(payload)

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 201:
            return response.json()['id']
        else:
            print(response.text)
            return None
