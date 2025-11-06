""" L = [8, 24,27, 48,2,16,9,102,7,84,91]
i = 0
c = 1
while c < len(L):
    if L[c]>L[i]:
        i = c
    c+=1
print (L[i])
d = 0
v = 1
while v < len (L):
    if L[v]<L[d]:
        d = v
    v+=1
print(L[d]) """
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
valeurmax = max(L)
valeurmin = min(L)
print("Max value:",valeurmax)
print("Min value:",valeurmin)
