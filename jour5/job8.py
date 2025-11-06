""" l = [8,24,27,48,2,16,9,7,84,91]
for val in l : 
    if val % 2==0:
        print(val)
 """



""" L =[1,2,4,7,9,10,11]
x=0
def value(x):
   while x in L:
     if x % 2 ==0:
        print(x)
x+=1
print(value(x)) """
L = [1, 2, 4, 7, 9, 10, 11]

def value(L):
    for x in L:
        if x % 2 == 0:
            print(x)

value(L)