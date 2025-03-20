class MercadoLivreAdvertisementDomain:

    def __init__(self, title: str, category_id: str, price: float, available_quantity: int, warranty: str,
                 domain: str, grid_id: str):
        self.site_id: None
        self.title: title
        self.family_name: None
        self.category_id = category_id
        self.official_store_id = None,
        self.price = price
        self.currency_id = "BRL"
        self.available_quantity = available_quantity
        self.buying_mode = "buy_it_now",
        self.listing_type_id = "gold_special",
        self.condition = "new"
        self.warranty = warranty
        self.catalog_product_id = None
        self.domain_id = domain,
        self.seller_custom_field = None
        self.automatic_relist = False,
        self.catalog_listing = False,

        self.channels = [
            "marketplace"
        ]
        self.sale_terms = []

        self.add_sales_term()
        self.attributes = []

    def add_sales_term(self):
        self.sale_terms.append({
            "id": "MANUFACTURING_TIME",
            "name": "Disponibilidade de estoque",
            "value_id": None,
            "value_name": "5 dias",
            "value_struct": {
                "number": 5,
                "unit": "dias"
            },
            "values": [
                {
                    "id": None,
                    "name": "5 dias",
                    "struct": {
                        "number": 5,
                        "unit": "dias"
                    }
                }
            ],
            "value_type": "number_unit"
        })

        self.sale_terms.append({
            "id": "WARRANTY_TYPE",
            "name": "Tipo de garantia",
            "value_id": "2230280",
            "value_name": "Garantia do vendedor",
            "value_struct": None,
            "values": [
                {
                    "id": "2230280",
                    "name": "Garantia do vendedor",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.sale_terms.append({
            "id": "WARRANTY_TIME",
            "name": "Tempo de garantia",
            "value_id": None,
            "value_name": "30 dias",
            "value_struct": {
                "number": 30,
                "unit": "dias"
            },
            "values": [
                {
                    "id": None,
                    "name": "30 dias",
                    "struct": {
                        "number": 30,
                        "unit": "dias"
                    }
                }
            ],
            "value_type": "number_unit"
        })

    def add_attributes(self, grid_id):
        self.attributes.append({
            "id": "GENDER",
            "name": "Gênero",
            "value_id": "110461",
            "value_name": "Sem gênero",
            "values": [
                {
                    "id": "110461",
                    "name": "Sem gênero",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "IS_SPORTIVE",
            "name": "É esportiva",
            "value_id": "242084",
            "value_name": "Não",
            "values": [
                {
                    "id": "242084",
                    "name": "Não",
                    "struct": None
                }
            ],
            "value_type": "boolean"
        })

        self.attributes.append({
            "id": "IS_SUITABLE_FOR_PREGNACY",
            "name": "É apta para gestação",
            "value_id": "242084",
            "value_name": "Não",
            "values": [
                {
                    "id": "242084",
                    "name": "Não",
                    "struct": None
                }
            ],
            "value_type": "boolean"
        })

        self.attributes.append({
            "id": "ITEM_CONDITION",
            "name": "Condição do item",
            "value_id": "2230284",
            "value_name": "Novo",
            "values": [
                {
                    "id": "2230284",
                    "name": "Novo",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "MAIN_MATERIAL",
            "name": "Material principal",
            "value_id": "466793",
            "value_name": "Algodão",
            "values": [
                {
                    "id": "466793",
                    "name": "Algodão",
                    "struct": None
                }
            ],
            "value_type": "string"
        })

        self.attributes.append({
            "id": "MODEL",
            "name": "Modelo",
            "value_id": None,
            "value_name": "Generica",
            "values": [
                {
                    "id": None,
                    "name": "Generica",
                    "struct": None
                }
            ],
            "value_type": "string"
        })

        self.attributes.append({
            "id": "RECOMMENDED_USES",
            "name": "Usos recomendados",
            "value_id": "-1",
            "value_name": None,
            "values": [
                {
                    "id": "-1",
                    "name": None,
                    "struct": None
                }
            ],
            "value_type": "string"
        })
        self.attributes.append({
            "id": "SALE_FORMAT",
            "name": "Formato de venda",
            "value_id": "1359391",
            "value_name": "Unidade",
            "values": [
                {
                    "id": "1359391",
                    "name": "Unidade",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "SIZE_GRID_ID",
            "name": "ID da guia de tamanhos",
            "value_id": None,
            "value_name": grid_id,
            "values": [
                {
                    "id": None,
                    "name": grid_id,
                    "struct": None
                }
            ],
            "value_type": "grid_id"
        })



