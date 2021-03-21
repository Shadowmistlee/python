"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:

Triangle Area formula:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

e.g.
Show:a ="
Input1:3

Show:b ="
Input2:4

Show:c ="
Input3:5

output:
perimeter: 12.000000
Area: 6.000000
"""
print('#此程式只適用於直角三角形#')
a = int(input('1'))
b = int(input('2'))
c = int(input('3'))
if (a+b)>=c:
    print('面積:',a*b/2)
    print('周長:',a+b+c)
else:
    print('what are you doing??????I already told you this program is only for Right triangle!!!!!')