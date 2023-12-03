import csv

# file_name = "jatin.csv"
# with open(file_name, mode="w") as csv_file:
# 	csv_writer = csv.writer(csv_file, delimiter=',')#  , quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 	csv_writer.writerow(["Name", "City"])
# 	csv_writer.writerow(["Jatin", "Udaipur"])
# 	csv_writer.writerows([["Aviral", "Zoetermeer"], ["Ram", "Den Haag"], ["Prashant", "Den Haag"]])
	

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



# employee_detail = []
# 0 -> name
# 1 -> Designation
# 2 -> Level
# 3 -> Salary

employe_detail_list = []

for key, value in nested_dict.items():
	employe_details = value
	# print(type(employe_details))
	for designations in employe_details:
		for designation, employees in designations.items():
			for employee in employees:
			# print(employee)
				for level, emp_details in employee.items():
					# print(level, emp_details)
					if isinstance(emp_details, list):
						# print(emp_details, level)
						for emp in emp_details:
							employee_data = []
							employee_data.append(emp["Name"])
							employee_data.append(designation)
							employee_data.append(level)
							employee_data.append(emp["Salary"])
							# print(emp["Name"],designation, level, emp["Salary"])
							employe_detail_list.append(employee_data)
					elif isinstance(emp_details, dict):
						# print(emp_details, level)
						employee_data = []
						employee_data.append(emp_details["Name"])
						employee_data.append(designation)
						employee_data.append(level)
						employee_data.append(emp_details["Salary"])
						employe_detail_list.append(employee_data)


file_name = "jatin.csv"
with open(file_name, mode="w") as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',')
	csv_writer.writerow(["Name", "Designation", "Level", "Salary"])
	csv_writer.writerows(employe_detail_list)