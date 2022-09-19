n=int(input())
for i in range(1,n):
    r=i*(i+1)
    if r==n:
        print("YES")
        break
else:
    print("NO")