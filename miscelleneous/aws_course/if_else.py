# x =5 
# y =10
# print(f"Number are x ={x} and y = {y}")

# z =x + y 

# print(f"Output is = {z}")


"""
if condition:
    you will do something
elif condition:
    do somthing
elif condition:
    do somthing
else:

"""

# number = 10
# if number > 20:
#     print("Number is greater than 5")
# else:
#     print("Outside If!!")


# percentage_marks = 86

# if percentage_marks > 90 :
#     print("Grade A")
# elif percentage_marks >= 80 and percentage_marks < 90:
#     print("Grade B")
# elif percentage_marks >= 70 and percentage_marks < 80:
#     print("Grade C")
# elif percentage_marks >= 60 and percentage_marks < 70:
#     print("Grade D")
# else:
#     print("Grade E")


# y = 1

# z = y**2 if y> 2 else y*10
# print(z)

# dummy_list = [2,3,4,5,6] 

# if 13 not in dummy_list:
#     print(13**2)


"""

*args
**kwargs
"""

def get_grade(percentage_marks):
    if percentage_marks > 90 :
        print("Grade A")
    elif percentage_marks >= 80 and percentage_marks < 90:
        print("Grade B")
    elif percentage_marks >= 70 and percentage_marks < 80:
        print("Grade C")
    elif percentage_marks >= 60 and percentage_marks < 70:
        print("Grade D")
    else:
        print("Grade E")


#get_grade(75)

name = "Bhanu"
comany = "Wipro"
project = "dummy2"

if name == "Bhanu" and comany == "Wipro" and project == "dummy":
    print("I know bhanu!!")
