from datetime import datetime
from datetime import timedelta
import sys


def main():
    """
    Prueba Desarrollador Python - OMNI.PRO
    Adrian Cuero
    andretti86@gmail.com

    * Fechas y Horas *

    Dada 2 fechas, A y B, en el formato:
        DD/MM/YYYY hh:mm:ss +xxxx

    * Imprimir el número de días Lunes, Martes, Miércoles, Jueves,
    Viernes, Sábados y Domingos que hay entre estas fechas.
    Asuma misma zona horaria.

    * Imprimir el número de horas laborales entre ese rango de
    fechas (no tomar en cuenta días feriados, asumir jornada de
    8hr/día, Lunes-Viernes). Asuma misma zona horaria.

    * Imprimir la diferencia entre las fechas (asuma misma zona
    horaria) en:
    - Segundos
    - Horas
    - Días

    * Realizar nuevamente el cálculo del punto anterior, utilizando
    fechas de diferentes zonas horarias.
    """
    formato = "%d/%m/%Y %H:%M:%S %z"
    temp_a = None
    temp_b = None
    fecha_a = None
    fecha_b = None
    

    while True:
        try:
            temp_a = datetime.strptime(input("Por favor ingrese Fecha A (DD/MM/YYYY hh:mm:ss +xxxx): "), formato)
        except ValueError:
            print("Error: Por favor ingrese una fecha con formato DD/MM/YYYY hh:mm:ss +xxxx")
            continue
        else:
            break
    
    while True:
        try:
            temp_b = datetime.strptime(input("Por favor ingrese Fecha B (DD/MM/YYYY hh:mm:ss +xxxx): "), formato)
        except ValueError:
            print("Error: Por favor ingrese una fecha con formato DD/MM/YYYY hh:mm:ss +xxxx")
            continue
        else:
            break


    if temp_a > temp_b:
        fecha_a = temp_b
        fecha_b = temp_a
    else:
        fecha_a = temp_a
        fecha_b = temp_b



    delta = fecha_b - fecha_a
    diferencia_dias = delta.days
    diferencia_horas = diferencia_dias * 24
    diferencia_segundos = diferencia_horas * 60


    horas_laborables = 0
    jornada_laboral = 8
    dias = {
        0:{"dia": "lunes", "veces": 0, "dia_laboral":True},
        1:{"dia": "martes", "veces": 0, "dia_laboral":True},
        2:{"dia": "miercoles", "veces": 0, "dia_laboral":True},
        3:{"dia": "jueves", "veces": 0, "dia_laboral":True},
        4:{"dia": "viernes", "veces": 0, "dia_laboral":True},
        5:{"dia": "sabado", "veces": 0, "dia_laboral":False},
        6:{"dia": "domingo", "veces": 0, "dia_laboral":False},
    }


    for i in range(diferencia_dias + 1):
        day = fecha_a + timedelta(days=i)
        dias[day.date().weekday()]['veces'] += 1;
        horas_laborables += jornada_laboral if dias[day.date().weekday()]['dia_laboral'] else 0
    

    print("Fecha A: {}".format(fecha_a))
    print("Fecha B: {}\n".format(fecha_b))
    
    print("Número de dias Lunes: {}.".format(dias[0]['veces']))
    print("Número de dias Martes: {}.".format(dias[1]['veces']))
    print("Número de dias Miércoles: {}.".format(dias[2]['veces']))
    print("Número de dias Jueves: {}.".format(dias[3]['veces']))
    print("Número de dias Viernes: {}.".format(dias[4]['veces']))
    print("Número de dias Sábado: {}.".format(dias[5]['veces']))
    print("Número de dias Domingo: {}.\n".format(dias[6]['veces']))

    print("Horas laborales: {} horas.".format(horas_laborables))
    print("Diferencia en segundos: {} segundos.".format(diferencia_segundos))
    print("Diferencia en horas: {} horas.".format(diferencia_horas))
    print("Diferencia en dias: {} dias.".format(diferencia_dias))
    sys.exit()



main()
# 06/05/2020 10:00:00 -08:00
# 21/07/2020 10:00:00 +05:00

