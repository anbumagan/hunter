n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
    if(l[i] in c):
        d.append(i)
    else:    
        c.append(l[i])
if(len(d)==0):
    print("unique")
else:
    print(l[d[0]])
