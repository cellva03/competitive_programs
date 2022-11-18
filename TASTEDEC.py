# cook your dish here
t = int(input())
while t:
    x,y = map(int,input().split())
    choco = 2*x
    candy = 5*y
    if choco > candy:
        print("Chocolate")
    elif choco == candy:
        print("Either")
    else:
        print("Candy")
    t-=1