import requests
from config import EVERYPIXEL_APIKEY as api_key
from config import EVERYPIXEL_APISECRET as api_secret

image_path = 'imgs/anc.jpg'

response = requests.post(
    'https://api.everypixel.com/v1/keywords',
    auth=(api_key, api_secret),
    files={'data': open(image_path, 'rb')},
    params={'num_keywords': 10} # 'lang': 'es', añadir como parámetro para mostrar keywords en español
)

if response.ok:
    tags = response.json()["keywords"]
    print('La imagen analizada muestra los siguientes porcentajes de similitud:')

    for tag_info in tags:
        confidence = tag_info["score"] # porcentaje de similitud con la palabra (valor entre 0 y 1)
        etiqueta = tag_info["keyword"]
        print(f"{(confidence*100):.2f}% con respecto a {etiqueta.upper()}")

else:
    print(f'Ha ocurrido un problema en la petición, corresponde a {response.status_code}-{response.reason}')