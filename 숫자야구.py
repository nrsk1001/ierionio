while True:
    a="665"
    c=str(input())
    s=0
    b=0

    for x in range(0,3):

        if a[x]==c[x]:

            s+=1

        else:

            for k in range(0, 3):

                if a[k] == c[x]:

                    b+=1

                    break
    print("%ds %db" % (s, b))
    if a==c:
        break
