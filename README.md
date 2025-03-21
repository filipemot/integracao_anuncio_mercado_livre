# Criação de Produtos(Camisetas) usando API do Mercado Livre

Cadastro Anúncios de Camisetas noMercado Livre usando a API

# Versão do Python
```bash
Python 3.9
```

# Atualizar Dependências
```bash
python.exe -m pip install --ignore-installed -r requeriments.txt
```

# Envs
- TOKEN=Token do Mercado Livre
- MERCADO_LIVRE_API_URL=Url da API
- MERCADO_LIVRE_API_SITE_ID=Exemplo: MLB  
- MERCADO_LIVRE_API_CURRENCY=Moeda do Anuncio Exemplo: BRL  
- MERCADO_LIVRE_API_CATEGORY_ID=Codigo da Categoria Exemplo: MLB31447  
- MERCADO_LIVRE_API_DOMAIN=Nome do Dominio Exemplo: MLB-T_SHIRTS  
- MERCADO_LIVRE_API_GRID_ID=ID Do Grid de Tamanhos
- MERCADO_LIVRE_API_SIZE_ID=Exemplo: 3259451

# Exemplos de Criação de Anuncios

Base dos códigos utilizados pelo mercado livre para a listagem de id's. Utilize o arquivo  base_categories_mercado_livre.json

```python
from domain.mercado_livre_advertisement_domain import MercadoLivreAdvertisementDomain
from domain.pictures_domain import PicturesDomain
from domain.variations_domain import VariationsDomain
from services.config_services import ConfigServices
from services.mercado_livre_services import MercadoLivreServices

config_services = ConfigServices()

def main():  
    mercado_livre_services = MercadoLivreServices(config_services.mercado_livre_api_url, config_services.token)  
    variations = [add_variation_yellow()]  
    mercado_livre_advertisement_domain = MercadoLivreAdvertisementDomain("Titulo", config_services.mercado_livre_api_category_id,  
                                                                         'Preco',  
                                                                         'Quantidade',  
                                                                         "Garantia",  
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
  
    return VariationsDomain(config_services.mercado_livre_api_site_id, "Amarelo", "Codigo da Cor",  
                            'Quantidade', "Tamanho", config_services.mercado_livre_api_grid_id, pictures)
```