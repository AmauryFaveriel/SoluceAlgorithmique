x1=int(input("Saisir x1 : "))
y1=int(input("Saisir y1 : "))
for x in range(1,x1+1) :
    for y in range(1,y1+1) :
        print("%2d x %2d = %2d "%(y, x, x*y), end='')
    print("\n")