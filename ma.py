nome = str(input('Diga o nome do aluno: '))
n1 = float(input('Diga a primeira nota do {}: '.format(nome)))
n2 = float(input('Diga a segunda nota do {}: '.format(nome)))

media = (n1 + n2) / 2

if media < 5.0:
    print('O aluno {} ficou com a media {:.1f} e esta REPROVADO '.format(nome, media))
elif media >= 5.0 and media <7.0 :
    print('O aluno {} esta com a media {:.1f} e esta de RECUPERAÇÃO '.format(nome, media))
elif media >= 7.0:
    print('O aluno {} esta com a media {:.1f} e foi APROVADO '.format(nome, media))
