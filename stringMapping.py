print("mapping:")
str="{}{}{}".format('hello','hi','welcome')
print(str)
str="{1}{0}{2}".format('hello','hi','welcome')
print(str)
str="{l}{f}{g}".format(g='hello',f='hi',l='welcome')
print(str)
print("alignment:")
str1="{:<20}{:^20}{:>20}".format('hello','hi','welcome')
print(str1)