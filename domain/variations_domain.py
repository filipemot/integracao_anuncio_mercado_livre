from domain.pictures_domain import PicturesDomain


class VariationsDomain:

    def __init__(self, domain: str, color: str, color_id: str, price: float, size: str , size_id: str,
                 pictures: [PicturesDomain]):
        self.domain = domain
        self.color = color
        self.color_id = color_id
        self.price = price
        self.size = size
        self.size_id = size_id
        self.pictures = pictures
