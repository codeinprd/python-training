
data_file_default = open("data.txt", mode="r")
# do certain things
data_file_default.close()

with open("data.txt") as reader:
  data = reader.read()

print(type(data))

print(reader.readlines())

#TODO: Print 3rd line from the input file
print(data[2])

