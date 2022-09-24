n1=int(input())
n2=int(input())
if n1>n2:
    n1,n2=n2,n1
n=n1+n2+100
t=n1+n2
l=[]
for i in range(t+1,n):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    if c==2:
        l.append(i)
print(l[0]-t)