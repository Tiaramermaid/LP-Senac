# calcular a media de N numeros 
# peça ao usuario para informar quantos numeros deseja inserir e, em
# seguida receba esses nmeros e exiba a media deles

soma = 0 
# 1. perguntar quantas notas deseja inserir
quant = int(input('quantas notas deseja inserir: '))
# 2. pedir as notas
for quant in range (1, quant + 1, 1):
    nota = int(input(f'digite a {quant} nota: '))
    soma = soma + nota 
# 3. calcular media (somar as notas e dividir pela quantidade)
media = soma/quant
# 4. exibir nota
print(f'sua media = {media}')