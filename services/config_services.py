import os

from dotenv import load_dotenv


class ConfigServices:

    def __init__(self):
        load_dotenv()

        self.token = os.getenv("TOKEN")
        self.mercado_livre_api_url = os.getenv("MERCADO_LIVRE_API_URL")
