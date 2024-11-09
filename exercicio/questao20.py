# Simular um caixa eletronico
# peça ao usuario o valor de um saque e exiba a quantidade de cedulas de
# 50, 20, 10 e 1 necessarias para o saque. considere que o valor sera sempre 
# um numero inteiro positivo

# 1. contador para armazenar meu dinheiro disponivel
# 2. perguntar se ele quer sacar ou depositar 
# 3. se ele quiser sacar exibir valor disponivel para saque
# 4. diminuir o Contador 
# 5. se ele quiser depositar exibir o valor disponivel 
# 6. dps do saque exibir o valor atual

saldo = 0 
pergunta = input('deseja Sacar ou Depositar?(S/D) (clique x para sair): ')
while pergunta != 'x':
    if pergunta == 'D':
        print (f'seu saldo: {saldo}')
        deposito = int(input('deseja depositar quanto?(50,20,10,1)'))
        saldo = saldo + deposito
        print(f'saldo atualizado: {saldo}')
        pergunta = input(f'deseja Sacar ou Depositar?(S/D): ')
    elif pergunta == 'S':
        print (f'seu saldo = {saldo}')
        saque = int(input('deseja sacar quanto?(50,20,10,1)'))
        saldo = saldo - saque
        print(f'saldo atualizado: {saldo}')
        pergunta = input(f'deseja Sacar ou Depositar?(S/D): ')
    else: 
        print('saindo')