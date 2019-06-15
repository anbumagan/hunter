n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if(int(l[i]+l[j])==0 or int(l[i]+l[j])==1):
            print(l[i],l[j])
        break  
