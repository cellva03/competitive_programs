t = int(input())
while t:
    x,p,q = map(int,input().split())
    print(x*(p-q))
    t-=1