"""
Topic:請使用input輸入要印制的箭頭大小
可利用字串乘法
e.g.
val="*" * 3
print(val)
***


1.Show:Please in row:
2.input:3
  *
 ***
*****
  *
  *
  *
"""
a=int(input('?'))
b=0
c=0
for n in range(1,a+1):
    print(' '*(a-b),'*'*(n+b))
    b+=1
while c<a:
    print(' '*(a),'*'*(1))
    c+=1