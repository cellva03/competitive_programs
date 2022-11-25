# cook your dish here
t = int(input())
while t:
    n = int(input())
    a, b, c, d = map(int,input().split())
    print(max(a,b,c,d))
    t-=1