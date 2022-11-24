# cook your dish here
t = int(input())
while t:
    x, y, z = map(int,input().split())
    reach = y//x
    if reach>z:
        print(0)
    else:
        print(z-reach)
    t-=1