x=int(input())
l=list(map(str,input().split()))
p=sorted(l)
print("".join(p[::-1]))
