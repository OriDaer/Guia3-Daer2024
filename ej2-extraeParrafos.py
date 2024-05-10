import requests
import pyperclip
from bs4 import BeautifulSoup
#https://dev.mysql.com/doc/refman/8.3/en/
url_pasado=''
while True:
    url_actual = pyperclip.paste()  # Obtener la URL del portapapeles
    if url_actual != url_pasado:  # Verifica si la URL es diferente a la anterior
        response = requests.get(url_actual)  # Obtener contenido HTML
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            parrafos = soup.find_all('p')
            p_text = []
            for p in parrafos:
                p_text.append(p.text)
                print(p_text)
            for texto in p_text:
                print(texto)
                url_pasado = url_actual  # Actualizar la URL anterior
        else:
            print(f"Error: {response.status_code}")
    else:
        print('URL actual es igual al anterior')