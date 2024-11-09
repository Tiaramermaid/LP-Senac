# contar numeros positivos insiridos pelo usuario 
# peça ao usuario para digitar repetidamente ate que ele digite 0
# exiba a quantidade de numeros positivos digitados

# 1. solicitar ao usuarios numeros ate que ele digite Zero
cont = 0
resposta = int(input('digite um numero: '))
while resposta >=1:
# 2. contar quantos numeros foram maiores que 0
    cont += 1
    resposta = int(input('digite um numero: '))
# 3. exibir o resultado
print(f'voce digitou {cont} numeros positivos')
