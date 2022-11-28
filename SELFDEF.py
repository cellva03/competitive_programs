def fun(li):
    c=0
    for i in li:
        if i <=10 and i >=60:
            c+=1
        else:
            continue
    return c

t = int(input())
while t:
    n = int(input())
    li = list(map(int,input().split()))
    count = filter(fun,li)
    print(count)