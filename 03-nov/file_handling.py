# execute this code from python/03-nov directory for a succesffult execution as it have certain
# relative paths and the code will brak if there are not there

# when my working directory is same as the location of the data file
data_file_default = open("data.txt", mode="r")
# print(data_file_default)# <_io.TextIOWrapper name='data.txt' mode='r' encoding='UTF-8'>
# when my working directory is different and I am fetching relative path
data_file_relative = open("03-nov-2023/data.txt")
# print(data_file_relative) #<_io.TextIOWrapper name='03-nov-2023/data.txt' mode='r' encoding='UTF-8'>
# when my working directory is different and I am fetching absolute path
data_file_absolute = open(
    "/Users/aviralvishnoi/Documents-local/work/classes/python/03-nov/data.txt"
)
# print(data_file_absolute) #<_io.TextIOWrapper name='/Users/aviralvishnoi/Documents-local/work/classes/python/03-nov/data.txt' mode='r' encoding='UTF-8'>
# print(data_file_default.readlines(60))
print(data_file_default.readlines())
# default file 
# data_default = data_file_default.read()
# # print(data_default)
# print("###########")
# data_file_default.close()
# print("###########")
# data_file_default = open("data.txt", mode="r")
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print("###########")
# data_file_default.close()
# print("###########")
# data_file_default = open("data.txt", mode="r")

# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_file_default.readline())
# print(data_default_rl)
# read file from relative path
# data_relative = data_file_relative.read()
# data_relative_rl = data_file_relative.read()
# print(data_relative)
# # read file with absolute path
# data_absolute = data_file_absolute.read()
# data_absolute_rl = data_file_absolute.read()
# print(data_absolute)




# File paths -->
# - absoulte path - /Users/aviralvishnoi/Documents-local/work/classes/python/03-nov/data.txt
# c:\users\aviralvishnoi\.....
# - relative path - 03-nov/data.txt


# python/03-nov/
