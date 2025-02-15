def imc(peso, altura):
    resultado = peso/altura **2
    return resultado

print("O IMC de uma pessoa com 1,74 de altura e 81kg é", imc(81, 1.74))

#-------------------------------------------------------------------------------------------------------------

from math import pi

"""

Função que calcula a área de uma forma geometrica plana, dadas as medidas da base e da altura e tipo da forma """

def calc_area(base, altura, tipo):
    match tipo:
        case"R": #Retangulo
            return base * altura
        case "T": #Triangulo
            return base * altura / 2
        case "E": #Ecliśe/circulo
            return (base/2) * (altura / 2) * pi
        case _: #Forma invalida
            return None
        

print(f"Area retangulo 22x47: {calc_area(22,47, 'R')}")
print(f"Area triangulo 12,5x25: {calc_area(12.5,25, 'T')}")
print(f"Area eclipse 20x30: {calc_area(20,30, 'E')}")
print(f"Area retangulo 8x11,5: {calc_area(8,11.5, 'R')}")
        
        