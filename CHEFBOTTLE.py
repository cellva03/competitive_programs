# cook your dish here
t = int(input())
while t:
    n, x, k = map(int,input().split())
    if (n*x) > k:
        print(k//x)
    else:
        print(n)
    t-=1