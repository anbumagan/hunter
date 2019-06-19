n,m=map(int,input().split())
l=list(map(int,input().split()))
c=[]
a1=[[abs(i-m),i]for i in l]
a1=sorted(a1)
a1=a1[1:]
a1=[i[1] for i in a1[:3]]
print(*a1)
