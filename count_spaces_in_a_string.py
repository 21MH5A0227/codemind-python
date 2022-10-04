n=input()
n=list(n)
v="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=0
for i in range(len(n)):
    if(n[i]==" "):
        c+=1
print(c)