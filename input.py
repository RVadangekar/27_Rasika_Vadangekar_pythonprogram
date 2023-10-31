count=0
while count<5:
    print(count)
    count=count+1
else:
        print(count)

a,b,c=map(int,input("enter number").split())
print("the numbers are:")
print(a,b,c)

l=list()
a=int(input("enter the size: "))
print("enter the element: ")
for i in range(0,a):
    l.append(int(input()))
print("list is : ",l)
