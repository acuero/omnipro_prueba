from datetime import datetime
import argparse
import os
import sys
import re
import mimetypes



def main():
    """
    Prueba Desarrollador Python - OMNI.PRO
    Adrian Cuero
    andretti86@gmail.com

    * Orden de palabras *
    Se le da un archivo de texto con el siguiente formato:
        4
        abc
        abcdefg
        abc
        bcdefg

    La primera línea contiene el número de palabras (n) que tiene el
    archivo. Las próximas n líneas contienen palabras (1 por línea),
    las cuales se pueden repetir a lo largo del archivo. Desarrolle un
    código que lea la información de dicho archivo de texto, y genere
    otro archivo de texto con lo siguiente:
        - En la primera línea debe mostrar el número de palabras
        distintivas.
        - En la segunda línea mostrar el número de ocurrencias de cada
        palabra distintiva.

    Para el ejemplo anterior, el formato del archivo final es el
    siguiente:
        3
        2 1 1

    Explicación: 3 palabras distintivas, abc se repite 2 veces, abcdefg
    1 vez y bcdefg 1 vez.
    """
    my_parser = argparse.ArgumentParser(
        prog='orden_palabras',
        description='Muestra cantidad de palabras distintivas y ocurrencia de cada una de estas.'
    )


    my_parser.add_argument(
        'Ruta',
        metavar='ruta',
        type=str,
        help='Ruta al archivo de texto'
    )


    args = my_parser.parse_args()
    ruta = args.Ruta
    if not os.path.exists(ruta):
        print("Error: La ruta especificada no existe.")
        sys.exit()
    
    if not os.path.isfile(ruta):
        print("Error: La ruta especificada no es de un archivo.")
        sys.exit()

    
    mime_type, none_type = mimetypes.guess_type(ruta)
    if mime_type != 'text/plain':
        print("Error: El archivo especificado no es de texto (*.txt).")
        sys.exit()


    with open(ruta, 'r') as reader:
        diccionario = []
        cantidad_palabras = None
        ocurrencias = {}

        for linea in reader:
            if not cantidad_palabras:
                cantidad_palabras = linea.rstrip()

                if re.match('^\\d+$', cantidad_palabras):
                    cantidad_palabras = int(cantidad_palabras)
                else:
                    print("Error: Se espera en la primera línea del archivo el número que representa la cantidad de palabras.")
                    sys.exit()
            else:
                palabra = linea.rstrip()

                if not palabra in ocurrencias:
                    ocurrencias[palabra] = 0
                
                ocurrencias[palabra] += 1
                diccionario.append(palabra)



    if not diccionario:
        print("Error: No se pudo recolectar palabras en el archivo.")
        sys.exit()
    
    
    if len(diccionario) != cantidad_palabras:
        print(
            """Advertencia: La cantidad de palabras especificada en la primera línea ({}) 
            no coincide con las palabras encontradas ({}).""".format(cantidad_palabras, len(diccionario))
        )
    

    distintivas = list(set(diccionario))
    archivo_final = "orden_palabras_{}.txt".format(datetime.today().strftime('%Y%m%d_%H%M%S'))

    with open(archivo_final, 'w') as writer:
        writer.write(str(len(distintivas)) + "\n")
        writer.write(" ".join(str(ocurrencia) for ocurrencia in ocurrencias.values()))
    
    print("orden_palabras: Fin del proceso.")
    print("orden_palabras: Los resultados los podrá ver en el archivo: {}".format(archivo_final))



main()
