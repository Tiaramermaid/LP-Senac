# Maior entre dois números
# Receba dois números e exiba qual deles é maior, ou diga se são iguais.

# 1. receber dois numeros 
numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
# 2. dizaer qual é o mair ou se sao iguais
if (numero2 == numero1):
    print('sao iguais')
if (numero1 > numero2):
    print(f'{numero1} é maior')
else:
    (f'{numero2} é maior')