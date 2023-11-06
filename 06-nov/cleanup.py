import os

students = ["bhanu", "krishna", "jatin", "lakshay", "sudheer"]

for student in students:
  file_name = f"06-nov/output_dir/{student}.txt"
  if os.path.exists(file_name):
    print(f"Deleting file {file_name}")
    os.remove(file_name)
    print(f"File {file_name} delete")
  else:
    print(f"File {file_name} doesnot exists")


directory_to_delete = "06-nov/output_dir"
os.rmdir(directory_to_delete)
