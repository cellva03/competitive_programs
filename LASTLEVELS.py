# cook your dish here
t = int(input())
while t:
    x, y, z = map(int,input().split())
    if x > 3:
        if x%3 == 0:
            rest = ((x//3)-1)*z
            print((x*y)+rest)
        else:
            rest = (x//3)*z
            print((x*y)+z)
    else:
        print(x*y)
    t-=1