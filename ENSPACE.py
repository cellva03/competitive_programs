# cook your dish here
t = int(input())
while t:
    n,x,y = map(int,input().split())
    res = x + (y*2)
    if res <=n:
        print("yes")
    else:
        print("no")
    t-=1