num=int(input())
l=list(map(str,input().split()))
l1=[]
m1=1
for i in range(len(l)):
    if(len(l[i])>m1):
        m1=len(l[i])
for j in range(len(l)):
    if(len(l[j])==m1):
        l1.append(l[j])
print(len(l1))