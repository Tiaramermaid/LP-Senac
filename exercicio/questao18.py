# verificar se um numero é Primo
# receba um numero inteirpo e verifiuqe se ele é primo (divisivel apenas por 1 e por ele mesmo)

# 1. solicitar um numero
numero = int(input('digite um numero: '))
# 2. verificar se ele é Primo
if numero %1 == numero and numero %numero == numero:
# 3. exibir resultado
    print('seu numero é primo')
else:
    print('numero nao primo')