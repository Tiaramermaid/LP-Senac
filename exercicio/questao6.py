# validaçao de senha simples
# o programa dev pedir uma senha e compara com a senha "1234"
# se a senha estiver correta, exiba "acesso permitido", senao exiba
# "senha incorreta"

# 1. definir senha
senha = 1234
# 2. solicitar senha
solic_senha = int(input("digite a senha: "))
# 3. verificar se é a senha correta
if solic_senha == senha :
# 4. exibir mensagem
    print('acesso permitido')
else:
    print('senha incorreta')