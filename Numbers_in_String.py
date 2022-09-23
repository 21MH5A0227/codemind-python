n=input()
s=0
d="0123456789"
for i in n:
    if i in d:
        s+=int(i)
print(s)