def fun(li):


t = int(input())
while t:
    n = int(input())
    li = list(map(int,input().split()))
    count = filter(fun,li)
    print(count)