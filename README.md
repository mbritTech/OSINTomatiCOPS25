# OSINTomatiCOPS25

> [!WARNING]  
> **Disponible** solamente durante esta **semana**

Muy buenas a todos, bienvenidos al repositorio de mi ponencia 
**"Ciberinteligencia y Programación, juntas para la acción"**.<br>
[**Aquí**](OsintomátiCOPS%20España%202025.pdf) podéis encontrar las correspondientes diapositivas y 
algunas indicaciones para el correcto uso de los diferentes scripts.

> [!NOTE]
> - Todas las herramientas utilizadas son totalmente **gratuitas**.<br>
> - En el fichero de [**configuración**](config.py) podéis encontrar las diferentes **claves** a
> modificar para el correcto funcionamiento de los scripts que utilizan **APIs**.<br>
> - Para el **registro** en estos **servicios** se pueden usar incluso **emails temporales**.

## Indicaciones para los scripts
### Desaparecidos
[**Script**](desaparecidos-CNDES.py)
- Es necesario tener **actualizada** la versión de **Python**.
- Instalar la **librería** correspondiente para **Web Scraping**
`pip install selenium`

### Reverse Whois
[**Script**](reverse-whois.py)
- Simplemente es necesario modificar el **fichero de configuración**
con las claves personales de la **API**.
- Tener instalada la **librería** para hacer **peticiones** a la **API**
`pip install requests`
- Este script genera un [**fichero**](ck-domains.txt) en el cual se **almacenan** los **dominios**
para que posteriormente se realice la **comprobación** de estos
con otro [**script**](ck-reverse-whois.sh) encargado de hacer un **whois** a cada uno ellos.

### Reconocimiento de Imágenes
[**Script Imagga**](imagga.py)<br>
[**Script Everypixel**](everypixel.py)
- Simplemente es necesario modificar el **fichero de configuración**
con las claves personales de la **API**.
- Tener instalada la **librería** para hacer **peticiones** a la **API**
`pip install requests`
- Tenéis unas **imágenes** de muestra en la siguiente [**carpeta**](imgs).

Espero que todo esto os sirva como punto de partida para 
crear vuestras propias herramientas.<br>
Un abrazo :)

**[manuelbrito.es](https://manuelbrito.es/)**
