t = int(input())
while t:
    x, y = map(int,input().split())
    res = ((x-1)//10) - ((y-1)//10)
    print(abs(res))
    t-=1