import pyperclip,requests
url_pasado=''
# https://www.gutenberg.org/cache/epub/1112/pg1112.txt
while True:
    url_actual = pyperclip.paste()  #obtengo la url del portapapeles
    if url_actual != url_pasado:  # verifico si la url es diferente a la anterior
        if url_actual.startswith("http"):#verifico si url es valida
            contenido = requests.get(url_actual)  # Obtener contenido HTML
            if contenido.status_code == 200:  # Verifica si la solicitud fue exitosa
                contenido = contenido.text.lower()  # obtener contenido HTML en forma de texto y convertir a minúsculas  
                num_archivos = 0 
                nombre_archivo = f"contenido_pa_{num_archivos + 1}.txt"# Nombre del archivo
                for texto in contenido:
                    archivo = open(nombre_archivo, 'w')# Guardar el contenido en un archivo de texto
                    archivo.write(contenido)
                    archivo.close()
            else:
                print('Error al obtener respuesta de la página.')
        else:
            print('La URL en el portapapeles no es válida.')
    else:
        print('La URL actual es igual a la anterior.')
