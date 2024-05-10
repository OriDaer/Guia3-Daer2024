#falta hacer que Finalmente los nombres de los archivos alojados en el sistema deben comenzar con un número asociado al número de descargas realizadas hasta el momento.
import pyperclip,requests
url_pasado=''
x=0
while True:
    url_actual = pyperclip.paste()  # Obtener la URL del portapapeles
    if url_actual != url_pasado:  # Verifica si la URL es diferente a la anterior
        contenido = requests.get(url_actual)  # Obtener contenido HTML
        if contenido.status_code == 200:  # Verifica si la solicitud fue exitosa
            contenido = contenido.text.lower()  # Convertir a minúsculas
            archivo = open('ej.txt', 'w')# Guardar contenido en archivo txt
        for texto in contenido :
            archivo.write(texto)#escribe en el archivo .txt
            url_pasado = url_actual  # Actualizar la URL anterior
        else:
            print('Error')
    else:
        print('URL actual es igual al anterior')