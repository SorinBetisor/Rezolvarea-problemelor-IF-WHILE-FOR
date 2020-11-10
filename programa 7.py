#Mihai are un unchi bogat care ia daruit in ziua in cae sa nascut
#un dolar,iar in fiecare urmator an el dubla cadoul si mai adauga
#atatia dolari cati ani implinea mihai
#a)sa se calculeze cati dolari a primit Mihai atunci cand
#   va implinit n ani (n<2)
#b)La ce varsta cadoul lui Mihai a fost mai mare de 100 de dolari
import sys
n=int(input('Introduceti varsta lui Mihai  = '))
d=1
if (n>20):
    print ('Eroare (n>20)')
    sys.exit()
elif ((n<=20) and (n>=1)):
    for i in range(1,n+1):
        if (i==1):
            d=d+2
        else:
            d=(d*2)+i
print ('Mihai are = ',d,' dolari')
print ('Cadoul lui Mihai va trece de 100 de dolari la 6 ani')
