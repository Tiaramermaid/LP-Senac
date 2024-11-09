# Calculo de desconto em compras
# peça o valor de uma copra. se o valor for maior que 100 reais,
# aplique um desconto de 10% e exibe o valor final.

desconto = 10/100
# 1. solicitar valor da compra
valor_compra = float(input('digite o valor da compra: '))
# 2. aplicar desconto de 10% se valor>100
if valor_compra > 100:
    valortotal = valor_compra - (valor_compra * desconto)
# 3. exibir o valor da compra 
    print(f'Valor Total com desconto: R${valortotal:.2f}')
else: 
    print(f'Valor Total: R${valor_compra:.2f}')