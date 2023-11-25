import json


"""
Reading a json file
file_object = open(file_name, “r”)
data = json.load(file_object)
json.load -> converts string to dict

"""

INPUT_FILE_PATH="example_json_file.json"


f_read = open(INPUT_FILE_PATH,"r")

#print(f_read)

records = json.load(f_read)

#print(type(records))

# print(type(records["data"]))
sum=0
for item in records["data"]:
    #@print(item["userId"],item["userName"],item["txnType"])
    #print(type(item))
    if item["txnType"] == "debit":
        sum= sum+ float(item["amount"].split("$")[1].replace(",",""))

print(sum)


