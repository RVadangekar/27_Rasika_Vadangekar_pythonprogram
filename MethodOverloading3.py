from multipledispatch import dispatch
@dispatch(int)
def add(a):
    print("value is zero")
@dispatch(int,int)
def add(a,b):
    print(a+b)
@dispatch(float)
def add(c):
    print(c/2)
add(10)
add(10,20)
add(10.20)
