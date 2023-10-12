a = 5
print(a, type(a))
a = "Kunal"
print(a, type(a))
a = True
print(a, type(a))


def function_name(parameter_1, parameter_2, parameter_n):
    # logic
    required_output = None
    return required_output


def area_of_square(side):
    area = side * side
    print("Inner Area of square is ", area)
    return area


def build_full_name(first_name, last_name):
    name = first_name + " " + last_name
    print("Concatenaation of ", first_name, "and", last_name, "is", name)
    return name


if __name__ == "__main__":
    side = 5
    area_outer = area_of_square(side)
    print("Outer Area of square is ", area_outer)
    full_name = build_full_name(first_name="Kunal", last_name="Pagare")
    print("Full name is ", full_name)
    first_name = "Aviral"
    last_name = "Vishnoi"
    full_name = build_full_name(first_name, last_name)
    print(f"concatenation of {first_name} and {last_name} is {full_name}")
