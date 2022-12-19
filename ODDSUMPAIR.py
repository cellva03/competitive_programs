for _ in range(int(input())):
    l = list(map(int,input().split()))
    odd = False
    even = False
    for i in l:
        if i % 2 == 0:
            even = True
        else:
            odd = True
    if odd and even:
        print("Yes")
    