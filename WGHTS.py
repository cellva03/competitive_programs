# cook your dish here
t = int(input())
while t:
    w, x, y, z = map(int,input().split())
    if (x+y) == w or (x+z) == w or (y+z) == w or x == w or y == w or z == w or (x+y+z) == w:
        print("yes")
    else:
        print("no")
    t-=1