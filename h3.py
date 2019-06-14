x=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i==l.index(i)):
        c.append(i)
print(*(sorted(c)))
if(len(c)==0):
    print(-1)
