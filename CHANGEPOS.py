t = int(input())
while t:
    a, b, c, d = map(int,input().split())
    if a != c and b != d:
        print(1)
    else:
        print(2)
    t-=1