t = int(input())
while t:
    x, y, z = map(int,input().split())
    if z >= abs(x-y):
        print("Yes")
    else:
        print("no")
    t-=1