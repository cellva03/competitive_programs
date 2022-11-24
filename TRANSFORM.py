# cook your dish here
t = int(input())
while t:
    x = int(input())
    res = x%3
    if res == 0 :
        print("NORMAL")
    elif res == 1:
        print("HUGE")
    else:
        print("SMALL")
    t-=1