#sa se scrie un program care va efectua
#a)adunarea a doua fractii date
#b)inmultirea a doua fractii date
#rezultatul va fi o fractie ireductibila
from fractions import Fraction
a=int(input('Dati numaratorul primei fractii (a)  = '))
b=int(input('Dati numitorul primei fractii (b)  = '))
c=int(input('Dati numaratorul celei de a doua fractii (c)  = '))
d=int(input('Dati numitorul celei de a doua fractii (d)  = '))
print('Suma fractiilor este = ',Fraction(a,b)+Fraction(c,d))
print('Produsul fractiilor este = ',Fraction(a,b)*Fraction(c,d))