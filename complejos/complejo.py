import math

"""
Prueba Desarrollador Python - OMNI.PRO
Adrian Cuero
andretti86@gmail.com

* Complejos *
Dado 2 números complejos, A y B, desarrollar un código que
imprima los valores de:
    - A+B
    - A-B
    - A*B
    - A/B
    - Mod(A)
    - Mod(B)

Para esta parte, deberá utilizar una clase, llamada Complejo, la
cual deberá inicializar con una parte real y una parte imaginaria, y tener
los métodos antes descritos. Por ejemplo:
    A = Complejo(2,1)
    B = Complejo(5,6)
    A+B → 7.0+7.0i
    A-B → -3.0-5.0i
    A*B → 4.00+17.00i
    A/B → 0.26-0.11i
    Mod(A) → 2.24+0.00i
    Mod(B) → 7.81+0.00i
"""

class Complejo(object):
    """Clase auxiliar para construir un número complejo."""

    def __init__(self, real, imag=0.0):
        """Constructor."""
        self.real = real
        self.imag = imag
    

    def __add__(self, other):
        """Método mágico para suma de complejos."""
        return Complejo(
            self.real + other.real,
            self.imag + other.imag
        )
    

    def __sub__(self, other):
        """Método mágico para resta de complejos."""
        return Complejo(
            self.real - other.real,
            self.imag - other.imag
        )
    

    def __mul__(self, other):
        """Método mágico para multiplicación de complejos."""
        return Complejo(
            self.real*other.real - self.imag*other.imag,
            self.imag*other.real + self.real*other.imag
        )
    

    def __div__(self, other):
        """Método mágico para división de complejos en python 2.x."""
        sreal = self.real
        simag = self.imag
        oreal = other.real
        oimag = other.imag
        r = float(oreal**2 + oimag**2)

        return Complejo(
            (sreal*oreal + simag*oimag) / r,
            (simag*oreal - sreal*oimag) / r
        )
    

    def __truediv__(self, other):
        """Método mágico para división de complejos en python 3.x."""
        sreal = self.real
        simag = self.imag
        oreal = other.real
        oimag = other.imag
        r = float(oreal**2 + oimag**2)

        return Complejo(
            (sreal*oreal + simag*oimag) / r,
            (simag*oreal - sreal*oimag) / r
        )
    

    def __abs__(self):
        """Método mágico para obtener módulo."""
        return Complejo(math.sqrt(self.real**2 + self.imag**2))
    


    def __str__(self):
        return "{:.2f}{}{:.2f}i".format(self.real, "+" if self.imag >= 0 else "", self.imag)





def main():
    # Solicitud de parte real y parte imaginaria para construir los números complejos
    real_a = None
    imag_a = None
    real_b = None
    imag_b = None

    # Parte real de A
    while True:
        try:
            real_a = float(input("Por favor ingrese la parte real de A: "))
        except ValueError:
            print("Error.")
            continue
        else:
            break
    
    # Parte imaginaria de A
    while True:
        try:
            imag_a = float(input("Por favor ingrese la parte imaginaria de A: "))
        except ValueError:
            print("Error.")
            continue
        else:
            break
    
    # Parte real de B
    while True:
        try:
            real_b = float(input("Por favor ingrese la parte real de B: "))
        except ValueError:
            print("Error.")
            continue
        else:
            break
    
    # Parte imaginaria de B
    while True:
        try:
            imag_b = float(input("Por favor ingrese la parte imaginaria de B: "))
        except ValueError:
            print("Error.")
            continue
        else:
            break
    
    complejo_a = Complejo(real_a, imag_a)
    complejo_b = Complejo(real_b, imag_b)
    suma = complejo_a + complejo_b
    resta = complejo_a - complejo_b
    multiplicacion = complejo_a * complejo_b
    division = complejo_a / complejo_b
    mod_a = abs(complejo_a)
    mod_b = abs(complejo_b)
    
    print("A= {}".format(complejo_a))
    print("B= {}\n".format(complejo_b))
    
    print("A+B -> {}".format(suma))
    print("A-B -> {}".format(resta))
    print("A*B -> {}".format(multiplicacion))
    print("A/B -> {}".format(division))
    print("Mod(A) -> {}".format(mod_a))
    print("Mod(B) -> {}".format(mod_b))





main()
