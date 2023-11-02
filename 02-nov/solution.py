

demo_dict = {
	"subjects": [
		{"math": [{"ram": 85}, {"krishna": 90}, {"bhanu": 95}]},
		{"physics": [{"ram": 75}, {"krishna": 77}, {"bhanu": 79}]},
		{"chemistry": [{"ram": 61}, {"krishna": 65}, {"bhanu": 69}]},
		{"computer_science": [{"ram": 57}, {"krishna": 71}, {"bhanu": 42}]},
		{"logical_reasoning": [{"ram": 42}, {"krishna": 88}, {"bhanu": 68}]},
	],
}

average_marks = {}

# average_marks = {
# 	"math": 3,
# 	"physics": 4,
# 	"chemistry": 5,
# 	"computer_science": 6,
# 	"logical_reasoning": 7
# }

for subject_details in demo_dict.values():
	# print(subjects)
	for subjects in subject_details:#subjects = {'math': [{'ram': 85}, {'krishna': 90}, {'bhanu': 95}]}
		# print(subjects)
		for subject, students in subjects.items():#subject = math, students = [{'ram': 85}, {'krishna': 90}, {'bhanu': 95}]
			# print(subject, students)
			total_marks = 0
			for student in students:#students = [{'ram': 85}, {'krishna': 90}, {'bhanu': 95}]  student = {'ram': 85}
				for name, marks in student.items():
					# print(name, marks)
					total_marks += marks
					# print(f"total marks : {total_marks}")
			average_mark = total_marks/len(students)
			# average_mark = total_marks/3 #wrong assumptions just in case if there are less students for a particular subject
			average_marks[subject] = average_mark
			# print(subject, total_marks)
			# print(average_marks)

# Get average marks in all subjects
# Average marks in maths is {average_mark}
# Average marks in physics is {average_mark}
# Average marks in chemistry is {average_mark}
# Average marks in computer_science is {average_mark}
# Average marks in logical_reasoning is {average_mark}


for subject_name, subject_average in average_marks.items():
	print(f"Average marks in {subject_name} is {subject_average}")

