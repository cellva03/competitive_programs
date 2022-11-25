# cook your dish here
t = int(input())
while t:
    a, b = map(int,input().split())
    if (21-(a+b)) <= 10:
        print(21-(a+b))
    else:
        print(-1)
    t-=1