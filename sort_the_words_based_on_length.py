n=input()
n=list(n.split(" "))
n.sort()
for i in range(len(n)):
    for j in range(i,len(n)):
        if(len(n[i])>len(n[j])):
            n[j],n[i]=n[i],n[j]
print(*n)