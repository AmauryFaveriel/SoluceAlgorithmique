print('Test de positivité de deux entiers.')
t = True
while t == True:
    r = ''
    x = 0
    y = 0
    while x <= 0 or y <= 0:
        x = int(input('Saisir x : '))
        y = int(input('Saisir y : '))
        if x>0 and y>0:
            print('Les deux nombres sont positifs.')
        else:
            print('Entrez deux nombres positifs.')
    while r != 'oui' and r != 'non':
        r=input('Voulez vous recommencer?\n')
        if r == 'oui':
            t = True
        elif r == 'non':
            t = False
        else:
            print('Réponse invalide, veuillez répondre oui ou non.')
