# Classificaçao de Notas
# receba uma nota de 0 a 10 e exiba:
#     aprovado>=7
#     recuperaçao (entre 5 e 6.9)
#     reprovado (nota<5)

# 1. receber nota
nota = float(input('digite a nota: '))
# 2. identificar situaçao
if nota < 5: 
# 3. exibir situaçao
    print('reprovado')
elif nota <= 6.9:
    print('recuperaçao')
else:
    print('Aprovado')