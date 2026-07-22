age = int (input("enter your age:"))
nationality = input("enter your nationality:")

if age >= 18:
    if nationality.lower() == "indian":
        print("Eligible to vote.")
    else:
        print("not eligible to vote (only indian citizen can vote).")
else:
    print("not Eligible to vote (age must be 18 or above).")    
