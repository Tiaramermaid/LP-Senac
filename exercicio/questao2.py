# Calculadora Simples
# O programa deve pedir dois números e uma operação (+, -, *, /) e exibir o resultado da operação entre os números.

# 1. pedir dois numeros
number = int(input('Digite o 1° numero :'))
number2 = int(input('Digite o 2° numero :'))

# 2. selecionar operaçao
operacao = input('selecione a operaçao (+, -, *, /): ')

# 3. executar os numeros coma operaçao selecionada
if (operacao == '+'):
    soma = number + number2
    print(number, '+', number2, '=', soma)
if (operacao == '-'):
    sub = number - number2
    print(number, '-', number2, '=', sub)
if (operacao == '*'):
    mult = number * number2
    print(number, '*', number2, '=', mult)
if (operacao == '/'):
    div = number / number2
    print(number, '/', number2, '=', div)
else: 
    print('error')
# 4. exibir o resultado
