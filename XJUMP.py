# cook your dish here
t = int(input())
while t:
    x, y = map(int,input().split())
    if x%y == 0:
        print(x//y)
    else:
        print((x//y)+(x%y))
    t-=1