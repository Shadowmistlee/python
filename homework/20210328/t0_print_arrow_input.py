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
def printHead(n):
    for l in range(1,n):
        print(" "*(n-l)+"*"*(1 if l==1 else 2*l-1))
printHead