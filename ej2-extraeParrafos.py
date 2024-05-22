import requests,pyperclip
from bs4 import BeautifulSoup
#https://dev.mysql.com/doc/refman/8.3/en/
url_pasado=''
while True:
    url_actual = pyperclip.paste() 
    if url_actual != url_pasado and url_actual.startswith("https"): 
        contenido = requests.get(url_actual)
        if contenido.status_code == 200:
            soup = BeautifulSoup(contenido.text, 'html.parser')
            parrafos = soup.find_all('p')
            p_text = []
            for p in parrafos:
                p_text.append(p.text)
                print(p_text)
            for texto in p_text:
                print(texto)
                url_pasado = url_actual 
        else:
            print(f"Error: {contenido.status_code}")
    else:
        print('URL actual es igual al anterior')