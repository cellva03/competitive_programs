for _ in range(int(input())):
    a, b, a1, b1, a2, b2 = list(map(int,input().split()))
    if((a == a1 and b == b1) or (a == b1 and b == a1)):
        