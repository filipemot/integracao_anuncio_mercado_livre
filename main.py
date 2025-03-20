from services.mercado_livre_services import MercadoLivreServices


def main():
    mercado_livre_services = MercadoLivreServices()
    mercado_livre_services.save_pictures('amarelo_1.png',
                                         'C:/Users/filip/Downloads/camisetasml/amarelo_1.png',
                                         'image/*')

if __name__ == '__main__':
    main()