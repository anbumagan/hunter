n=int(input())
l=list(map(int,input().split()))
c={}
for i in l:
    c[i]=l.count(i)
for i in c:
    if(c[i]==1):
        print(i,end=" ")
