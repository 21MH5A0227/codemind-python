def boo(n):
    c=str(n)
    c=list(c)
    a=0
    for i in range(len(c)):
        k=int(c[i])
        if(k==0):
           continue
        if(n%k==0):
           a+=1
    if(a==len(c)):
       return True
    return False
a=int(input())
b=int(input())
n=[]
for i in range(a,b+1):
    if(boo(i)==True):
       n.append(i)
print(*n)
    
        
        