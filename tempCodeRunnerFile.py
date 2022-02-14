
def imc(peso, altura):
    return peso / (altura ** 2)

'''print(f'Peso: 89, altura: 1.75, IMC: {imc(89, 175)}') #f na frente da str é possível abrir chave e colocar um código dentro'''

p = input('Qual o peso?')
a = input('Qual é a altura?')

print(f'Peso: {p}, altura: {a}, IMC: {imc(p, a)}')