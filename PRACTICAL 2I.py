m1 = float(input("enter marks of subject 1:"))
m2 = float(input("enter marks of subject 2:"))
m3 = float(input("enter marks of subject 3:"))

total = m1 + m2 + m3
percentage = total / 100

print("Total =",total)
print("Percentage =",percentage)

if percentage >=90:
    grade = "A+"
elif percentage>=80:
    grade = "A"
elif percentage>=70:
       grade = "B"
elif percentage>=60:
    grade = "C"
elif percentage>=40:
        grade ="D"
else:
    grade = "fail"
    
    print("Grade =",grade)
