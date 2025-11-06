L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
val = 90
lav =25
n = 0
while n < len(L):
    if L[n]< lav:
        del L[n]
    elif L[n] >val:
        del L[n]
    else:
        n+=1
print(L)
resultat = 1
for x in L:
    resultat*=x
print(resultat)

    
    
""" if nombre < lav:
        del L [nombre]
    elif nombre > lav:
        nombre * lav
    elif nombre > val:
        del L[nombre]
    elif nombre < val:
        nombre * val
    nombre+=1
print(L) """

             

        



