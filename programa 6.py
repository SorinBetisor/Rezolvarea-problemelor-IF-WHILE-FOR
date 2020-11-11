#Se da numarul natural n. Sa se compare sumele S1 si S2 unde
#a) S1=1^3+2^3+...+n^3 si S2=(1+2+...+n)^2
#b) S1=3(1^2+2^2+...+n^2) si S2=n^3+n^2+(1+2+...+n)
n=int(input('Dati n = '))
#a)
s1=0
s2=0
s3=0
s4=0
p=n
for i in range (1,n+1):
    s1=s1+(i**3)
    s2=s2+i
s2a=s2**2
if (s2a>s1):
    print('a) A doua suma (S2) este mai mare')
elif (s2a==s1):
    print('a) Sumele S1 si S2 sunt egale')
elif (s1>s2a):
    print('a) Prima suma (S1) este mai mare')
#b)
for j in range (1,p+1):
    s3=s3+(i**2)
    s4=s4+i
s3a=s3*3
s4a=s4+(n**3)+(n**2)
if (s4a>s3a):
    print('b) A doua suma (S2) este mai mare')
elif (s3a==s4a):
    print('b) Sumele S1 si S2 sunt egale')
elif (s3a>s4a):
    print('b) Prima suma (S1) este mai mare')




