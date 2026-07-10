#Method 1:Using third variable
a = 10
b = 20
print("before swap(method 1):",a,b)
temp = a
a = b
b = temp
print("After swap(method 1):",a,b)

#Method 2:tuple unpacking
x = 100
y = 200
print("\nbefore swap(method2):",x,y)
x,y = y,x
print("after swap(method2):",x,y)
