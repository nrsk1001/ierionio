import math
count = 1005-int(input())
c=0
d=0
f = open("result.txt", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,7):
    for g in range(1005,count,-1):
        a[int((lines[g].split())[i])] +=1
for t in range(45):
    print(str(t+1)+":"+str(a[t+1]))
print(a)
print(b)
for y in range(1,46):
    c += a[y]
for l in range(1,46):
    d+=(a[l]-c/45)*(a[l]-c/45)
print(math.sqrt(d/45))
print(c/45)
