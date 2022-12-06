# cook your dish here
for _ in range(int(input())):
    x, y = map(int,input().split())
    print("YES") if (y*30)<=x else print("no")