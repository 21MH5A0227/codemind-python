a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
s=0
for i in range(len(l)):
    if i==0 or i==len(l)-1:
        continue
    else:
        l[i].pop(0)
        l[i].pop(-1)
        s+=sum(l[i])
print(s)