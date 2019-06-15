n,m=map(int,input().split())
l=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(0,m):
        if(l[i]==l[j]):
            c=c+1
if(c==m):            
    print("YES")
else:
    print("NO")
