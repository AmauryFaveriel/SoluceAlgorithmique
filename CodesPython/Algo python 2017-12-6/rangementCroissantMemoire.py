x=int(input('Saisir x :'))
y=int(input('Saisir y :'))
if x==y:
    print('Les deux nombres sont égaux')
elif x>y:
    x,y=y,x
    print('L\'ordre est',x,y)
else:
    print('L\'ordre est',x,y)
