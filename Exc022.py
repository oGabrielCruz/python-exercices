nome = str(input('Qual o seu nome?: ')).strip()
print('\nSeu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras que seu nome possui: {}'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras que seu primeiro nome possui: {}'.format(nome.find(' ')))