f = open("result.txt", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(46):
    for i in range(1,7):
        for g in range(len(lines)):
            a[int((lines[g].split())[i])] +=1
for t in range(45):
    print(str(t+1)+":"+str(a[t+1]))
print(a)
for y in range(1,46):
    for l in range(1,46):
        a[y]<=a[l]
