from domain.mercado_livre_advertisement_domain import MercadoLivreAdvertisementDomain
from domain.pictures_domain import PicturesDomain
from domain.variations_domain import VariationsDomain
from services.config_services import ConfigServices
from services.mercado_livre_services import MercadoLivreServices

config_services = ConfigServices()


def main():
    mercado_livre_services = MercadoLivreServices(config_services.mercado_livre_api_url, config_services.token)
    variations = [add_variation_yellow(), add_variation_green(), add_variation_pink(), add_variation_white(),
                  add_variation_black()]
    mercado_livre_advertisement_domain = MercadoLivreAdvertisementDomain("Camiseta Teste",
                                                                         config_services.mercado_livre_api_category_id,
                                                                         50,
                                                                         50,
                                                                         "Garantia do vendedor: 30 dias",
                                                                         config_services.mercado_livre_api_domain,
                                                                         config_services.mercado_livre_api_grid_id,
                                                                         variations,
                                                                         config_services.mercado_livre_api_site_id,
                                                                         config_services.mercado_livre_api_currency,
                                                                         ["Descrição"],
                                                                         mercado_livre_services)
    result = mercado_livre_services.save_advertisement(mercado_livre_advertisement_domain)

    if result is not None:
        print("Anuncio criado com sucesso")
    else:
        print("Erro ao criar anuncio")


def add_variation_yellow():
    pictures = [PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\amarelo_1.png", "amarelo_1.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\amarelo_2.png", "amarelo_2.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\amarelo_3.png", "amarelo_3.png")]

    return VariationsDomain(config_services.mercado_livre_api_site_id, "Amarelo", "52007",
                            100.0, "Unico", config_services.mercado_livre_api_grid_id, pictures)


def add_variation_green():
    pictures = [PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\verde_1.png", "verde_1.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\verde_2.png", "verde_2.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\verde_3.png", "verde_3.png")]

    return VariationsDomain(config_services.mercado_livre_api_site_id, "Verde", "52014",
                            100.0, "Unico", config_services.mercado_livre_api_grid_id, pictures)


def add_variation_pink():
    pictures = [PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\rosa_1.png", "rosa_1.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\rosa_2.png", "rosa_2.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\rosa_3.png", "rosa_3.png")]

    return VariationsDomain(config_services.mercado_livre_api_site_id, "Rosa", "2450312",
                            100.0, "Unico", config_services.mercado_livre_api_grid_id, pictures)


def add_variation_white():
    pictures = [PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\branco_1.png", "branco_1.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\branco_2.png", "branco_2.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\branco_3.png", "branco_3.png")]

    return VariationsDomain(config_services.mercado_livre_api_site_id, "Rosa", "2450308",
                            100.0, "Unico", config_services.mercado_livre_api_grid_id, pictures)


def add_variation_black():
    pictures = [PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\preto_1.png", "branco_1.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\preto_2.png", "preto_2.png"),
                PicturesDomain("C:\\Users\\filip\\Downloads\\camisetasml\\preto_3.png", "preto_3.png")]

    return VariationsDomain(config_services.mercado_livre_api_site_id, "Preto", "52049",
                            100.0, "Unico", config_services.mercado_livre_api_grid_id, pictures)


if __name__ == '__main__':
    main()
