str="welcome"
arr1=bytes(str,'utf-8')
print(arr1)

arr2= bytearray("hello",'utf-8')
print(arr2)

z = memoryview(arr2)
print(z[1])
 
