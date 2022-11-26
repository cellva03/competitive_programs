# cook your dish here
t = int(input())
while t:
    a, b, x, y = map(int,input().split())
    if a < b:
        print("yes") if (a+x)>=b else print("no")
    else:
        print("yes") if (a-y)<=b else print("no")
    t-=1