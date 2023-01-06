vowels = ['a','e','i','o','u']
for _ in range(int(input())):
   n = int(input())
   s = input()
   
   res = False
   c=0
   
   for i in s:
      if i not in vowels:
            c += 1
      else:
            c = 0
      
      if c >=4:
            res = True
   if(res):
        print("No")            
