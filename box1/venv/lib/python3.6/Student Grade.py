import random
l=["Math", "English", "Science"]
name= input("Enter First Name Last Name")
for loop in l:
    gpa=random.randint(255,400)/100
    if gpa <=2.5:
        print("You failed this class")
    elif gpa >=2.6 and gpa<= 3.0:
        print("You get a B")
    elif gpa >=3.0:
        print("You get an A")




print("your name is", name, "with class", l[0], "and gpa ", gpa)
print("your name is", name, "with class", l[1], "and gpa ", gpa)
print("your name is", name, "with class", l[2], "and gpa ", gpa)