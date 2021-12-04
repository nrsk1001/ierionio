a,b,c=map(int,input().split())

if b<c:
    d = a // (c - b)
    print(d+1)

if b>=c:
    print(-1)
