def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
num1 = int(input("輸入第一個數字: "))
num2 = int(input("輸入第二個數字: "))

print( num1,"和", num2,"的最小公倍數為", lcm(num1, num2))