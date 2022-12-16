# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int,input().split())
    res = float(x+y)//2
    if res > z:
        print("Yes")
    else:
        print("No")