#Se dau numerele reale pozitive a  c. Sa se verifice daca exist un triunghi
#ale carui laturi au lungime (in aceeasi unitate de masura) egale cu a,b,c
#in caz afirmativ,sa se determine tipul triunghiului: echilateral,isoscel,scalen

a=float(input('Dati latura a  = '))
b=float(input('Dati latura b  = '))
c=float(input('Dati latura c  = '))
if ((a<b+c) and (b<a+c) and (c<a+b)):
    print('Exista asa triunghi')
    if ((a==b==c)):
        print ('Triunghiul este echilateral')
    elif (((a==b) and (a!=c)) or ((b==c) and (b!=a)) or ((a==c) and (a!=b))):
        print ('Triunghiul este isoscel')
    elif (a!=b!=c):
        print ('Triunghiul este scalen')
else:
    print('Nu exista un triunghi cu asemenea laturi')

