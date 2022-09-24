import math as m
def fun(n):
    if n<2:
        return False
    for i in range(2,int(m.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
x=0
a=int(input())
b=int(input())
for s in range(a,b+1):
    if fun(s):
        x=x+1
print(x)