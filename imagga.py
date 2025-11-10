import requests
from config import IMAGGA_APIKEY as api_key
from config import IMAGGA_APISECRET as api_secret

image_path = 'imgs/anc.jpg'  # situar imagen en la misma carpeta del script

response = requests.post(
    'https://api.imagga.com/v2/tags',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb'), 'limit': 10} # 'language': 'es', para mostrar keywords en español
)

if response.ok:
    tags = response.json()["result"]["tags"]
    print('La imagen analizada muestra los siguientes porcentajes de similitud:')

    for tag_info in tags:
        confidence = tag_info["confidence"]
        etiqueta = tag_info["tag"]["en"] # cambiar si se va a utilizar otro idioma para las keywords
        print(f"{confidence:.2f}% con respecto a {etiqueta.upper()}")

else:
    print(f'Ha ocurrido un problema en la petición, corresponde a {response.status_code}-{response.reason}')
