# cook your dish here
for _ in range(int(input())):
    x , y = map(int,input().split())
    print(0) if x >= y else print(y-x)
    