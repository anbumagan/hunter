n=str(input())
c=1
for i in range(len(n)-1):
    a=int(n[i]+n[i+1])
    if(a<=26 and n[i]!="0"):
        c=c+1
if(c==3):        
    print(c)
else:
    print(c+(c-1)//2) 
