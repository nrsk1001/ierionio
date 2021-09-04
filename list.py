b=[1,2,3,4,5]
while True:
    a = int(input("1~4"))
    if a==1:
        c=int(input())
        b.append(c)
    if a==2:
        e=int(input())
        if e in b:
            b.remove(a)
    if a==3:
        print(b)
    if a==4:
        break
