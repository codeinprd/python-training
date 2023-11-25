import time

start_time = time.time()


nested_dict = {
    "Employees": [
        {
            "Managers": [
                {
                    "L1": [
                        {"Name": "Madhav Chaudhary", "Salary": 2208000},
                        {"Name": "Arshdeep Garg", "Salary": 2505000},
                    ],
                    "L2": {"Name": "Ishan Rawat", "Salary": 3200000},
                    "L3": {"Name": "Mahendra Sharma", "Salary": 5000000},
                }
            ],
            "Developers": [
                {
                    "FrontEnd": [
                        {"Name": "Saurav Singh", "Salary": 400000},
                        {"Name": "Sachin Agarwal", "Salary": 500000},
                        {"Name": "Ajit Goyal", "Salary": 675000},
                    ],
                    "BackEnd": [
                        {"Name": "Irfan Ali", "Salary": 989000},
                        {"Name": "Robin Pandey", "Salary": 1100000},
                    ],
                }
            ]
        }
    ]
}
# json_dict = nested_dict.json_dict

# Integers used to calculate the sum of salaries of all the managers
l1_manager_sum, l2_manager_sum, l3_manager_sum = (0, 0, 0)

for employee in nested_dict.get("Employees"):
    # print(employee)
    for designation, emp_details in employee.items():
        if designation == "Managers":
            if isinstance(emp_details, list):
                for emp_detail in emp_details:
                    if isinstance(emp_detail, dict):
                        for level, details in emp_detail.items():
                            if level == "L1":
                              if isinstance(details, list):
                                for detail in details:
                                    print(detail)
                                    

            elif isinstance(emp_details, dict):
                # TODO: build logic to extract values from dictionary
                pass
            else:
                print("Error -> Datatype other than list or is not expected here")


# for manager in nested_dict.get("Employees")[0].get("Managers"):
#     for classes, values in manager.items():
#         if classes == "L1":
#             for salaries in values[:]:
#                 for names, salary in salaries.items():
#                     if names == "Salary":
#                         l1_manager_sum += salary
#         elif classes in ("L2"):
#             for name, salary in values.items():
#                 if name == "Salary":
#                     l2_manager_sum += salary
#         elif classes in ("L3"):
#             for name, salary in values.items():
#                 if name == "Salary":
#                     l3_manager_sum += salary

# print(f"L1 Manager salary is : {l1_manager_sum}")
# print(f"L2 Manager salary is : {l2_manager_sum}")
# print(f"L3 Manager salary is : {l3_manager_sum}")

print("--- %s seconds ---" % (time.time() - start_time))
