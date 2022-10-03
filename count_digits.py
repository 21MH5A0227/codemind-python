num=int(input())
l=list(map(str,input().split()))
l1=[]
s="+-"
for i in range(len(l)):
    if("-" in l[i] or "+" in l[i]):
        l1.append(len(l[i])-1)
    else:
        l1.append(len(l[i]))
for j in range(len(l)):
    print(l1[j],end=" ")