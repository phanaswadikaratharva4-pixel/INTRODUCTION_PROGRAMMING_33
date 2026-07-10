#IMPLICIT TYPE CONVERSION
a = 10
b = 2.5
result = a + b
print("Implicit Conversion (int + float):",result)
print("TYPE:",type(result))

# Explicit type conversion (correct usage)
x = 10
y = "5"
y = int(y)
result2 = x + y
print("\nExplixit Conversion (int + str converted to int):",result2)
