for _ in range(int(input())):
    w, x, y, z = map(int,input().split())
    if ((y*z)+x) > x :
        print("overflow")
    elif ((y*z)+x) < x:
        print("unfilled")
    else:
        