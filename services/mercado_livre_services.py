import json
from typing import Optional, Any

import requests


class MercadoLivreServices:
    bearer = 'Bearer '

    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token

    def save_pictures(self, name: str, path: str, extension: str) -> Optional[Any]:
        url = f"{self.url}/pictures/items/upload"

        files = {'file': (name, open(path, 'rb'), extension)}

        headers = {
            'Authorization': self.bearer + self.token
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
            'Content-Type': 'application/json',
            'Authorization': self.bearer + self.token
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 201:
            id_advertisement = response.json()['id']
            self.save_description(mercado_livre_advertisement, id_advertisement)

            return id_advertisement

        else:
            print('Anuncio nao criado', response.text)
            return None

    def save_description(self, mercado_livre_advertisement: any, id_advertisement: str) -> Optional[Any]:
        url = f"{self.url}/items/{id_advertisement}/description"

        payload = json.dumps({'plain_text': mercado_livre_advertisement.descriptions}, ensure_ascii=False)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.bearer + self.token
        }
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 201:
            return response.json()
        else:
            print('Descricao nao criada', response.text)
            return None
