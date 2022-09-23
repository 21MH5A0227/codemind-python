d="0123456789"
for i in range(int(input())):
    s=input()
    for i in s:
        if i in d:
            print("Yes")
            break
    else:
        print("No")