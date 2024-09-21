'''print('qual a sua idade')
idade = int(input())

if idade >=18:
    print('Acesso liberado!beba com moderação')
else:
    print('Acesso negado você é menor de idade')'''


# código para liberar acesso apenas para maiores de 19 idade anos

'''print('qual a sua idade?')

if idade < 18:
    print('Acesso negado! Volte pra casa')
elif idade == 18:
    print('Ainda não tem acesso! Você é menor de idade!')
else:
    print('Acesso liberado! Você já pode encher a cara')'''





# codigo para verificar se o aluno está aprovado 

'''print('digite as notas do primeiro bimestre:')  
B1 = float(input())
print('digite a nota do segundo bimestre:') 
B2 = float(input())
print('digite a nota do terceiro bimestre:')
B3 = float(input())
print('digite a nota do quarto bimestre:')
B4 = float(input())
media = (B1 + B2 + B3 + B4) / 4
print('a media do aluno é ', media) 

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('recuperacao')
else:
    print('reprovado')'''

# código para verificar se pode participar do mulheres tech

'''print('Qual o seu gênero ?  (F ou M)')
genero = input()
print('qual municipio você mora?') 
municipio = input()

if genero == 'F' and municipio == 'Rio de Janeiro':
    print('você pode participar')
else:
    print('Não pode participar')'''


    # Criar código para programa que libera acesso á um filme para maiores de 18 anos

print('Filme para maiores de 18 anos ou adolescentes acompanhados dos pais ')

print('Qual a sua idade ?')
idade = int(input())

if idade > 18:
    print('Entrada liberada')
elif idade > 15:
    print('O FILME SELECIONADO É PRA MAIORES DE 18 ANOS\nPARA ACESSAR COM RESPONSAVÉL')
    responsavel = input(). upper() 
    responsavel == 'sim'
    print('Acesso liberado! BOM FILME\nAproveite nossos combro de pipoca ')
else:
    print('Acesso Negado')