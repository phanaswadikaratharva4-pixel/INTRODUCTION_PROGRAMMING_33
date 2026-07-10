age = input("enter your age:")
marks = input("neter the marks:")

# display orignal types
print("\nbefore conversation:")
print("age:",age, "type:",type(age))
print("marks:",marks,"type:",type(marks))

#type conversation (casting)
age = int(age)
marks = float(marks)
#performing arithmatic operations
future_age = age + 5
total_marks = marks + 10
print("\nafter conversion:")
print("age (int):",age)
print("marks (float):",marks)
print("\narithmatic opersations:")
print("age after 5 years:",future_age)
print("marks after bonus:",total_marks)
