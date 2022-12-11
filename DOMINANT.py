for _ in range(int(input())):
    l = list(map(int,input().split()))
    maxi = max(l)
    l.remove(maxi)
    if maxi > (l[0]+l[1]):
        print("Yes")
    else:
        print("No")