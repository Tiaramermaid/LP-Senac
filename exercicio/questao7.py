# verificar se um numero esta em um intervalo
# receba um numero e exiba se ele esta entre 10 e 50(inclusive)

# 1. solicitar numero
numero = int(input('digite um numero: '))
# 2. verificar se esta entre 10 e 50(se ele é maior que 10 e menor que 50)
if numero < 50 and numero > 10:
# 3. exibir resultado
    print('seu numero esta entre a seleçao!!')
else:
    print('nao foi dessa vez :(')