'''Função que calcula a área de uma forma geométrica específica'''
from math import pi
def calcular_area(base, altura, forma):
    if forma == 'R':   #Retângulo
        return base * altura
    elif forma == 'T':  #Triângulo
        return base * altura / 2
    elif forma == 'E':   #Elipse
        return (base / 2) * (altura / 2) * pi #Número PI
    else: #Forma desconhecida
        return None

#print(f"Retângulo 15x25: {calcular_area(15, 25, 'R')}")
#print(f"Triângulo 12x16: {calcular_area(12, 16, 'T')}")
#print(f"Elipse 10x20: {calcular_area(10, 20, 'E'):.2f}")

b = float(input('Difite o valor da base: ')) 
a = float(input('Digite o valor da altura: '))
f = str(input('Digite a inicial da forma: ')).upper()

print(f"base: {b}, altura: {a}, a área é {calcular_area(b, a, f)}")

