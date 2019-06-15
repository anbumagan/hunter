x=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
if(len(l1)%2==0):
    while(len(l1)!=0):
        print(max(l1),end=" ")
        print(min(l1),end=" ")
        l1.remove(max(l1))
        l1.remove(min(l1))
else:
    while(len(l1)!=0):
        if(len(l1)!=1):
            print(max(l1),end=" ")
            print(min(l1),end=" ")
            l1.remove(max(l1))
            l1.remove(min(l1))
        else:
            print(*l1,end=" ")
            break
