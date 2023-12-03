import csv

males_in_class = 0
females_in_class = 0
# file_name_with_path = "/Users/aviralvishnoi/Documents-local/work/classes/python/25-nov/source_file.csv"
file_name = "source_file.csv"
with open(file_name) as csv_file:
    csv_data = csv.reader(csv_file)
    for data in csv_data:
        if data[4] == "male":
            males_in_class += 1
            # males_in_class = males_in_class + 1
        elif data[4] == "female":
            females_in_class += 1
        else:
            print("I am the header")

print(f"Number of males in class are {males_in_class}")
print(f"Number of females in class are {females_in_class}")

with open(file_name) as csv_file:
    csv_data = csv.reader(csv_file)
    i = 0
    for data in csv_data:
        if i == 0:
            print(data)
            i = 1
            continue
        if data[4] == "male":
            print(data[0])
        else:
            print(data[0])
