#se dau numerele naturale m si n unde m<n
#sa se verifice daca n este o putere
#a lui m
m=int(input('Dati numarul natural m (baza) = '))
n=int(input('Dati numarul natural n (puterea) = '))
if (n<m):
    print('Eroare - Conform conditiei: m<n')
else:
    a=True
    for i in range(1,n+1):
        if(m**i==n):
            print('Da,',n,' este putere a lui ',m)
            a=False
    if a:
        print('Nu,',n,' nu este putere a lui ',m)