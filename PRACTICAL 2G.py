
km = float(input("Enter kilometers: "))
celsius = float(input("Enter temperature in Celsius: "))
rupees = float(input("Enter rupees: "))

meters = km * 1000
fahrenheit = (celsius * 9/5) + 32
dollars = rupees / 85

print("Meters =", meters)
print("Fahrenheit =", fahrenheit)
print("US Dollars =", round(dollars, 2))
