n=int(input())
l=list(map(int,input().split()))
c=max(l)
for i in range(0,n-1):
    for j in range(i+1,n):
        if(abs(l[i]+l[j])<c):
            a,b=l[i],l[j]
            c=abs(a+b)
print(a, b) 
       
