t = int(input())
while t:
    n = int(input())
    s = str(input())
    res = ''
    for i in s:
        if i == 'A':
            res+='T'
        elif i == 'T':
            res+='A'
        elif i == 'G':
            res+='C'
        elif i == 'C':
            res+= 'G'
    print(res)
    t-=1
