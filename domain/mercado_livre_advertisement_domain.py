from domain.pictures_domain import PicturesDomain
from domain.variations_domain import VariationsDomain
from services.mercado_livre_services import MercadoLivreServices


class MercadoLivreAdvertisementDomain:

    def __init__(self, title: str, category_id: str, price: float, available_quantity: int, warranty: str,
                 domain: str, grid_id: str, variations: [VariationsDomain], site_id: str, currency_id: str,
                 descriptions: [str], mercado_livre_services: MercadoLivreServices):
        self.site_id = site_id
        self.title = title
        self.family_name: None
        self.category_id = category_id
        self.official_store_id = None
        self.price = price
        self.currency_id = currency_id
        self.available_quantity = available_quantity
        self.buying_mode = "buy_it_now"
        self.listing_type_id = "gold_special"
        self.condition = "new"
        self.warranty = warranty
        self.catalog_product_id = None
        self.domain_id = domain
        self.seller_custom_field = None
        self.automatic_relist = False
        self.catalog_listing = False

        self.channels = [
            "marketplace"
        ]
        self.sale_terms = []

        self.__add_sales_term()
        self.attributes = []
        self.grid_id = grid_id
        self.__add_attributes(grid_id)
        self.variations = variations
        self.mercado_livre_services = mercado_livre_services
        self.descriptions = descriptions
        self.add_variations(variations)

    def add_variations(self, variations: [VariationsDomain]):
        self.variations = []
        for variation in variations:
            pictures = self.__add_pictures(variation.pictures)
            self.__add_variations(variation.color, variation.color_id, variation.price, variation.size,
                                  variation.size_id, self.grid_id, pictures)

    def __add_pictures(self, pictures: [PicturesDomain]):
        pictures_ids = []
        for picture in pictures:
            picture_id = self.mercado_livre_services.save_pictures(picture.name, picture.path, "image/*")
            if picture_id:
                pictures_ids.append(picture_id)
        return pictures_ids

    def __add_variations(self, color: str, color_id: str, price: float, size: str,
                         size_id: str, grid_id: str, pictures: []):
        self.variations.append({
            "price": price,
            "attribute_combinations": [
                {
                    "id": "COLOR",
                    "name": "Cor",
                    "value_id": color_id,
                    "value_name": color,
                    "values": [
                        {
                            "id": color_id,
                            "name": color,
                            "struct": None
                        }
                    ],
                    "value_type": "string"
                },
                {
                    "id": "SIZE",
                    "name": "Tamanho",
                    "value_id": size_id,
                    "value_name": size,
                    "values": [
                        {
                            "id": size_id,
                            "name": size,
                            "struct": None
                        }
                    ],
                    "value_type": "string"
                }
            ],
            "available_quantity": 10,
            "sold_quantity": 0,
            "sale_terms": [],
            "picture_ids": pictures,
            "attributes": [
                {
                    "id": "SIZE_GRID_ROW_ID",
                    "value_name": f"{grid_id}:1"
                }
            ]
        })

    def __add_sales_term(self):
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

    def __add_attributes(self, grid_id):
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

        self.attributes.append({
            "id": "SLEEVE_TYPE",
            "name": "Tipo de manga",
            "value_id": "466804",
            "value_name": "Curta",
            "values": [
                {
                    "id": "466804",
                    "name": "Curta",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "T_SHIRT_COLLAR_TYPE",
            "name": "Tipo de gola",
            "value_id": "466787",
            "value_name": "Redonda",
            "values": [
                {
                    "id": "466787",
                    "name": "Redonda",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "WEDGE_SHAPE",
            "name": "Forma de caimento",
            "value_id": "-1",
            "value_name": None,
            "values": [
                {
                    "id": "-1",
                    "name": None,
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "WITH_RECYCLED_MATERIALS",
            "name": "Com materiais reciclados",
            "value_id": "-1",
            "value_name": None,
            "values": [
                {
                    "id": "-1",
                    "name": None,
                    "struct": None
                }
            ],
            "value_type": "boolean"
        })

        self.attributes.append({
            "id": "EMPTY_GTIN_REASON",
            "name": "EMPTY_GTIN_REASON",
            "value_id": "17055161",
            "value_name": "Outro motivo",
            "values": [
                {
                    "id": "17055161",
                    "name": "Outro motivo",
                    "struct": None
                }
            ],
            "value_type": "string"
        })

        self.attributes.append({
            "id": "GARMENT_TYPE",
            "name": "Tipo de roupa",
            "value_id": "12038970",
            "value_name": "Camiseta",
            "values": [
                {
                    "id": "12038970",
                    "name": "Camiseta",
                    "struct": None
                }
            ],
            "value_type": "list"
        })

        self.attributes.append({
            "id": "BRAND",
            "name": "Marca",
            "value_id": "276243",
            "value_name": "Genérica",
            "values": [
                {
                    "id": "276243",
                    "name": "Genérica",
                    "struct": None
                }
            ],
            "value_type": "string"
        })

    def to_json(self):
        return {
            "site_id": self.site_id,
            "title": self.title,
            "family_name": None,
            "category_id": self.category_id,
            "user_product_id": None,
            "official_store_id": self.official_store_id,
            "price": self.price,
            "currency_id": self.currency_id,
            "available_quantity": self.available_quantity,
            "sale_terms": self.sale_terms,
            "buying_mode": self.buying_mode,
            "listing_type_id": self.listing_type_id,
            "condition": self.condition,
            "attributes": self.attributes,
            "variations": self.variations,
            "warranty": self.warranty,
            "catalog_product_id": self.catalog_product_id,
            "domain_id": self.domain_id,
            "seller_custom_field": self.seller_custom_field,
            "automatic_relist": self.automatic_relist,
            "catalog_listing": self.catalog_listing,
            "channels": self.channels,
            "descriptions": self.descriptions
        }
