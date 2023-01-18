for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print('010')
    elif n >= 4:
        for i in range(0,n):
            if i == 0:
                print('1',end='')
            elif i == 1:
                print('0',end='')
