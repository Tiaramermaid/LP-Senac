# Verificar se um numero é multiplo de 3 e 5 
# peça um numero e verifique se ele é divisivel por 3 e 5 
# ao mesmo tempo.

# 1. solicitar o numero 
numero = int(input('digite um numero: '))
# 2. verificar se ele é divisivel por 3 e 5 
if numero % 3 == 0 and numero % 5 == 0:
# 3. exibir resultado
    print('seu numero é multiplo de 3 e 5')
else:
    print('seu numero nao é multiplo de 3 e 5')