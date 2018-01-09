print('Division euclidienne de deux entiers')
a=int(input('Saisissez le dividende :'))
b=int(input('Saisissez le diviseur :'))
q=int(a/b)
r=a-b*q
print('Le quotient de',a,'par',b,'vaut',q)
print('Le reste de',a,'par',b,'vaut',r)