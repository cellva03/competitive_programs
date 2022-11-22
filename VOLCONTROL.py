# cook your dish here
t = int(input())
while t:
    x, y = map(int,input().split())
    print(abs(x-y))
    t-=1