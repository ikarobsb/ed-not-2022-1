""" Função para calcular o IMC """
'''peso = float(input('Digite o seu peso'))
altura = float(input('Digite a sua altura'))'''

def imc(peso, altura): # estrutura da função --> def + nome da função + parâmetros da função
    return peso / (altura ** 2) # cálculo da função

'''print(f'Peso: 89, altura: 1.75, IMC: {imc(89, 175)}') #f na frente da str é possível abrir chave e colocar um código dentro'''

p = float(input('Qual o peso? ')) # entrada de dados
a = float(input('Qual é a altura? ')) # entrada de dados
i = imc(p, a) # chamada da função
print(f'Peso: {p}, altura: {a}, IMC: {i:.3f}')



