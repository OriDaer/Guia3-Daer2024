import requests, pyperclip
from bs4 import BeautifulSoup
#https://www.python.org/about/help/
url_pasada=''
while True:
    url = pyperclip.paste() 
    if url != url_pasada and url.startswith("https"): 
        archivo = requests.get(url)#obtengo/traigo archivo de http
        if archivo.status_code == 200:
            contenido = archivo.text
            arr = []
            soup = BeautifulSoup(contenido, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                    if link['href'].startswith('http'):
                        arr.append(link['href'])
                        print(arr)
        else:
            print(f"Error: {archivo.status_code}")
