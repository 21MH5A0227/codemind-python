s=input()
v="aeiou"
l=[]
for i in s:
    if i in v:
        l.append(i)
l=set(l)
l=list(l)
if(len(l)==5):
    print("True")
else:
    print("False")