x=int(input())
l=list(map(int,input().split()))
rep=[]
for i in range(len(l)):
    k=i+1 
    for j in range(k,len(l)):
        if(l[i]==l[j] and l[i] not in rep):
            rep.append(l[i])
print(*(sorted(rep)))
