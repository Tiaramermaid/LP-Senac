#verificar se um numero é par ou impar 
#Peça ao usuário para digitar um número inteiro e exiba se ele é par ou ímpar.

# 1. ler um número inteiro
number = int(input("Digite um numero inteiro: "))
# 2. verificar se é par ou impar 
if (number %2 == 0):
# 3. exibir o resultado
    print('par')
else: 
    print('impar')