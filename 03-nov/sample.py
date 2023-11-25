
data_file_default = open("data.txt", mode="r")
# do certain things
data_file_default.close()

with open("data.txt") as reader:
  data = reader.read()

print(type(data))

print(reader.readlines())

#TODO: Print 3rd line from the input file
print(data[2])


import time


def func_a():
  
  #TODO: Logic
  end_time = time.time()
  time_taken = end_time - start_time
  print(f"Time taken  is {time_taken} seconds")


start_time = time.time()
func_a()
print(f"Time taken  is {time.time() - start_time} seconds")

