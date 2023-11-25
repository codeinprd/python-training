import json


INPUT_DATA = "input_json.json"

f = open(INPUT_DATA)
data = json.load(f)

# print(data)
for item in data["records"]:
    print(item)

f_out = open("demo_output.json","w")
json.dump(data,f_out)