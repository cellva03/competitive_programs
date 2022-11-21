t = int(input())
while t:
    x,y,z = map(int,input().split())
    print(((x*2)+(y*2))*z)
    t-=1