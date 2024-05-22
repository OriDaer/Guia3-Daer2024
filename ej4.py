import requests,pyperclip,os
from bs4 import BeautifulSoup
#https://indi.ei.udelar.edu.uy/
url_anterior=''
while True:
    url = pyperclip.paste()  
    if url != url_anterior: 
        if 'https' in url:
            contenido = requests.get(url)
            if contenido.status_code == 200:
                soup = BeautifulSoup(contenido.text, 'html.parser') #analiza el contenido html con beautifulsoup
                pdf_links = []
                for link in soup.find_all('a', href=True): #encuentra todos los <a href> que contengan '.pdf'
                    href = link['href']
                    if '.pdf' in href:
                        pdf_links.append(href)
                    else:
                        print('No se encuentran .pdf en tu enlace')
                print(pdf_links)
                carpeta = './Descargas' #ruta de la carpeta a crear
                if not os.path.exists(carpeta): #si la carpeta no existe,la crea
                    os.makedirs(carpeta) #crea carpeta
                    print(f'El subdirectorio creado es: {carpeta}')
                else:
                    print(f'El subdirectorio {carpeta} ya existe.')
                for pdf_link in pdf_links:  #descarga y guarda cada pdf en la carpeta
                    contenido = requests.get(pdf_link) #obtiene el contenido del pdf
                    contenido.raise_for_status()
                    nombre_archivo = os.path.basename(pdf_link) #obtengo el nombre del archivo pdf
                    ruta_archivo = os.path.join(carpeta, nombre_archivo) #crear la ruta completa del archivo
                    archivo_pdf = open(ruta_archivo, 'wb') #abre un archivo en escritura binaria para escribir el pdf alli
                    archivo_pdf.write(contenido.content) #escribo el pdf en el archivo
                    archivo_pdf.close() #cierro el archivo después de escribir en él
                    print(f"Descarga exitosa: {nombre_archivo} en {carpeta}")
            else:
                print('Algo salió mal')
        print('Url no valido')