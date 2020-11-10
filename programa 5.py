#conform calendarului japonez,fiecare an poarta denumirea unui animal
#fiecare denumire se repeta exact o data la 12 ani
#deci un ciclu este format din denumirile
#1sobolan 2bou 3tigru 4iepure 5dragon 6sarpe 7cal 8oaie 
# 9maimuta 10cocos 11caine 12porc
#sa se scrie un algoritm care va citi de la tastatura anula si va arata
#denumirea conform calendarului japonez
a=int(input('Introduceti anul = '))
if a%12==8:
    print('Dragon')
if a%12==7:
    print('Iepure')
if a%12==6:
    print('Tigru')
if a%12==5:
    print('Bou')
if a%12==4:
    print('Sobolan')
if a%12==9:
    print('Sarpe')
if a%12==10:
    print('Cal')
if a%12==11:
    print('Oaie')
if a%12==0:
    print('Maimuta')
if a%12==3:
    print('Porc')
if a%12==2:
    print('Caine')
if a%12==1:
    print('Cocos')