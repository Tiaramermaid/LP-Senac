# clasificaçao de idade 
# criança(ate 12 anos)
# adolescente (de 13 a 17 anos)
# adulto >18

idade = int(input('digite sua idade para verificar sua faixa etaria: '))

if (idade >= 13) and (idade <= 17):
    print('adolescente')
elif idade <= 12 :
    print('criança')
else:
    print('adulto')