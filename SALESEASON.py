for _ in  range(int(input())):
    x = int(input())
    if 100>=x:
        print(x)
    elif x > 100 and x<=1000:
        print(x-25)
    elif x > 1000 and x <= 5000:
        print(x-100)
    else:
        