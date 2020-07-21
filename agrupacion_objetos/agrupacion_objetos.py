import sys
import csv
import json



def main():
    """
    Prueba Desarrollador Python - OMNI.PRO
    Adrian Cuero
    andretti86@gmail.com

    * Agrupación de objetos *
    Dado una serie de productos con los siguientes parámetros:
        - Nombre (Letras y números)
        - Código de barras (sólo números)
        - Fabricante (sólo letras)
        - Categoría (sólo letras)
        - Género (Masculino o Femenino)

    Desarrollar una función que retorne un diccionario con la serie de
    objetos agrupados por: Fabricante → Categoría → Género, como se
    ilustra en el siguiente ejemplo:

    Producto 1:
        - Nombre: Zapatos XYZ
        - Código de barras: 8569741233658
        - Fabricante: Deportes XYZ
        - Categoría: Zapatos
        - Género: Masculino

    Producto 2:
        - Nombre: Zapatos ABC
        - Código de barras: 7452136985471
        - Fabricante: Deportes XYZ
        - Categoría: Zapatos
        - Género: Femenino

    Producto 3:
        - Nombre: Camisa DEF
        - Código de barras: 5236412896324
        - Fabricante: Deportes XYZ
        - Categoría: Camisas
        - Género: Masculino

    Producto 4:
        - Nombre: Bolso KLM
        - Código de barras: 5863219635478
        - Fabricante: Carteras Hi-Fashion
        - Categoría: Bolsos
        - Género: Femenino

    Resultado:
    {
        "Deportes XYZ": {
            "Zapatos": {
                "Masculino": [Producto 1],
                "Femenino": [Producto 2]
            },
            "Camisas": {
                "Masculino": [Producto 3]
            }
        },
        "Carteras Hi-Fashion": {
            "Bolsos": {
                "Femenino": [Producto 4]
            }
        }
    }
    """
    diccionario = {}
    with open('productos.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        for linea in csv_reader:
            if linea['fabricante'] not in diccionario:
                diccionario[linea['fabricante']] = {}
            
            if linea['categoria'] not in diccionario[linea['fabricante']]:
                diccionario[linea['fabricante']][linea['categoria']] = {}
            
            if linea['genero'] not in diccionario[linea['fabricante']][linea['categoria']]:
                diccionario[linea['fabricante']][linea['categoria']][linea['genero']] = []
            
            diccionario[linea['fabricante']][linea['categoria']][linea['genero']].append(linea)
    

    print("Diccionario: ", json.dumps(diccionario, indent=2))
    sys.exit()



main()
