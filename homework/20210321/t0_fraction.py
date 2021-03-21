"""
Topic:輸入分子及分母，確認是否等於 350/450:

Show:Please input numerator"
Input1:70

show:Please input Denominator:
Input2:90
Output:True

Input1:6
Input2:9
Output:False
"""
a = int(input('分子'))
b = int(input('分母'))
if a/b == 350/450:
    print('yes')
else:
    print('no')