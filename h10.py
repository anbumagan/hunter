n,m=map(int,input().split())
l1={int(a) for a in input().split()}
b1={int(b) for b in input().split()}
if(b1.issubset(l1)):
    print("YES")
else:
    print("NO")
