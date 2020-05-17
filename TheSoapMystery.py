import bisect
n =int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
for i in range(q):
    query=int(input())
    print(bisect.bisect_left(a,query))
