# "w" mode
# "a" mode
# "x" mode


# writer = open("06-nov/lecture_output.txt", "w")
# writer.write("This is a demo file")
# writer.close()


# appender = open("06-nov/lecture_output_appender.txt", "a")
# appender.write("This is a demo file which appends data\n")
# appender.close()


# new_file = open("06-nov/new.txt", "a")
# new_file.write("demo")
# new_file.close()
# /Users/aviralvishnoi/Documents-local/work/classes/python
# /Users/aviralvishnoi/Documents-local/work/classes/python/demo


# students = ["bhanu", "krishna", "jatin", "lakshay"]
# #bhanu.txt

# for student in students:
#   file_name = f"06-nov/{student}.txt"
#   print(file_name)
#   file_writer = open(file_name, "w")
#   print(file_writer)
#   file_writer.write(f"{student} is awesome!")
#   file_writer.close()


students_characteristics = {
  "bhanu": "reporter",
  "sudheer": "tester",
  "jatin": "etl developer",
  "lakshay": "etl developer",
  "krishna": "tester"
}

for student, domain in students_characteristics.items():
  file_name = f"06-nov/{student}.txt"
  message = f"{student} is a {domain}!"
  with open(file_name, "a") as writer:
      writer.write(message)

num_var = 1
for student, domain in students_characteristics.items():
  file_name = f"06-nov/developers.txt"
  message = f"{num_var}. {student} is a {domain}!\n"
  with open(file_name, "a") as writer:
      writer.write(message)
  num_var += 1


# creator= open("06-nov/dummy.txt", "x")
