s=str(input())
stack=[]
s1=""
for i in range(len(s)):
    stack.append(s[i])
while(len(stack)):
    s1=s1+stack.pop()
if(s==s1):
    print("YES")
else:
    print("NO")
