#Taking two inputs
a = input("Enter first value:")
b = input("Enter second value:")
#checking if both are numeric
if a.replace('.',",1).isdigit() and b.replace('.',",1).isdigit():
    a = float(a)
    b = float(b)
    result = a + b 
    print("\nBoth inputs and numeric.")
    print("Sum:",result)
elif a.isalpha() and b.isalpha():
    result = a + b
    print("\nboth inputs are strings.")
    print("concatenation:",result)
else:
    print("\nvalid input types. cannot perform operation.")    
