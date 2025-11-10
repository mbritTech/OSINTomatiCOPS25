from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# --- Configuración del navegador ---
# Asegúrate de que el ejecutable de ChromeDriver está en tu PATH o especifica la ruta
# Si usas un driver manager, no necesitas especificar la ruta del ejecutable
# service = webdriver.ChromeService(executable_path='/ruta/a/chromedriver')
# driver = webdriver.Chrome(service=service)

# Para versiones modernas de Selenium, el driver se gestiona automáticamente
driver = webdriver.Chrome()

# --- URL de la web a scrapear ---
url = 'https://cndes-web.ses.mir.es/publico/Desaparecidos/'

try:
    # 1. Navegar a la página
    print("Navegando a la página...")
    driver.get(url)
    time.sleep(7)  # Espera para que la página cargue completamente

    print("Haciendo scroll en la página...")
    ActionChains(driver).scroll_by_amount(0,600).perform()

    # 2. Extracción del texto de las fichas
    print("Extrayendo información inicial...")
    info_fichas = driver.find_elements(By.CLASS_NAME, 'fichaDesc') # elemento principal con toda la información
    print(f"Se encontraron {len(info_fichas)} fichas.")
    time.sleep(5)

    informacion_inicial = []
    for ficha in info_fichas:
        informacion_inicial.append(ficha.text.split("\n"))

    for contador, texto in enumerate(informacion_inicial):
        print(f"\n--- Ficha inicial {contador + 1} ---")

        # Mostrando solamente la información necesaria
        print(texto[0])
        print(texto[1].split("+")[0])

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cierra el navegador al final
    print("\nProceso completado. Cerrando el navegador.")
    driver.quit()