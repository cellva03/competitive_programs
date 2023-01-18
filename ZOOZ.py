l = [3,1,4,7,9,5,10,8]
l=sorted(l)
for i in range(0,l[len(l)-1]):
    if (i+1) not in l:
        print(i+1) 


