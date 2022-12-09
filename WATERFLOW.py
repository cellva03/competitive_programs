# cook your dish here
for _ in range(int(input())):
    w, x, y, z = map(int,input().split())
    if ((y*z)+w) > x :
        print("overflow")
    elif ((y*z)+w) < x:
        print("unfilled")
    else:
        print("filled")