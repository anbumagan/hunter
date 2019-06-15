from itertools import permutations
s=str(input())
s1=permutations(s)
for i in list(set(s1)):
    print(''.join(i))
