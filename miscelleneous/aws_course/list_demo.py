def return_input_list():
    print("IN FIRST FUNCTION ")
    salary = [ "$100", "$200", "$1200","#3200","#2500"]
    print("END OF  FIRST FUNCTION ")
    return salary


def do_formating(emp_salary:list):
    print("IN SECOND FUNCTION ")
    emp_output_list = []

    for item in emp_salary:
        if "$" in item:
            item_formated = int(item.split("$")[1])
            print(item_formated)
            emp_output_list.append(item_formated)
        elif "#" in item:
            item_formated = int(item.split("#")[1])
            print(item_formated)
            emp_output_list.append(item_formated)
        else:
            print("")

    print("END OF  2nd FUNCTION ")
    return emp_output_list


def get_output(output_list: list):
    print("Start OF  3rd FUNCTION ")
    print(output_list)
    print(sum(output_list))
    print("END OF  3rd FUNCTION ")



if __name__ == "__main__":
    print("start OF  MAIN FUNCTION ")
    ouptu_sal_list = return_input_list()
    output_list = do_formating(ouptu_sal_list)
    get_output(output_list)
    print("END OF  MAIN FUNCTION ")


developers = ["Aviral", "Ram", "Bhanu", "Jatin", "Sudheer", "Kunal", "Krishna"]