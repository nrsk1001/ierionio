a,b=map(int,input().split())
if 10000>=b>=-10000:
    if  10000>=a>=-10000:
        if a>b:
            print(">")
        if a<b:
            print("<")
        if a==b:
            print("==")
