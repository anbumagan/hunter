x=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(x):
    ls=l[i:]
    m=max(ls)
    if(l[i] == m):
        d.append(l[i])
print(*d)
print(max(d))
