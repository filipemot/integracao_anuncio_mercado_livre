import os

from dotenv import load_dotenv


class ConfigServices:

    def __init__(self):
        load_dotenv()

        self.token = os.getenv("TOKEN")
        self.mercado_livre_api_url = os.getenv("MERCADO_LIVRE_API_URL")
        self.mercado_livre_api_site_id = os.getenv("MERCADO_LIVRE_API_SITE_ID")
        self.mercado_livre_api_currency = os.getenv("MERCADO_LIVRE_API_CURRENCY")
        self.mercado_livre_api_category_id = os.getenv("MERCADO_LIVRE_API_CATEGORY_ID")
        self.mercado_livre_api_domain = os.getenv("MERCADO_LIVRE_API_DOMAIN")
        self.mercado_livre_api_grid_id = os.getenv("MERCADO_LIVRE_API_GRID_ID")
        self.mercado_livre_api_size_id = os.getenv("MERCADO_LIVRE_API_SIZE_ID")


