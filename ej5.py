import requests,pyperclip,os
from bs4 import BeautifulSoup
# https://listado.mercadolibre.com.ar/
# https://listado.mercadolibre.com.ar


url_pasado=''
while True:
    url = pyperclip.paste()
    if not url.endswith('/'): #chequeo que la url termine en "/"
        url += '/'  #agrego "/" al final de la url en caso de no estar
    producto= input('ingrese el nombre del producto a buscar')
    url = f"{url}{producto.replace(' ', '-')}"# Construyo la url de ml
    print(url)
    if url != url_pasado and url.startswith("https"): 
        contenido = requests.get(url)
        if contenido.status_code == 200:
            conten_links=[]
            producto = input('Ingrese el producto a buscar')
            url_ml = f"{url}{producto.replace(' ', '-')}" #url a buscar en ml
            soup = BeautifulSoup(contenido.text, 'html.parser')
            #codigo
            #crea y subir info al subdirect
            carpeta = './Descargas' #ruta de la carpeta a crear
            if not os.path.exists(carpeta): #si la carpeta no existe,la crea
                os.makedirs(carpeta) #crea carpeta
                print(f'El subdirectorio creado es: {carpeta}')
            else:
                print(f'El subdirectorio {carpeta} ya existe.')
            for conten_link in conten_links:  #descarga y guarda cada pdf en la carpeta
                contenido = requests.get(conten_link) #obtiene el contenido del pdf
                contenido.raise_for_status()
                nombre_archivo = os.path.basename(conten_link) #obtengo el nombre del archivo pdf
                ruta_archivo = os.path.join(carpeta, nombre_archivo) #crear la ruta completa del archivo
                archivo_pdf = open(ruta_archivo, 'wb') #abre un archivo en escritura binaria para escribir el pdf alli
                archivo_pdf.write(contenido.content) #escribo el pdf en el archivo
                archivo_pdf.close() #cierro el archivo después de escribir en él
                print(f"Descarga exitosa: {nombre_archivo} en {carpeta}")
        else:
            print('Algo salió mal')
    print('Url no valido')