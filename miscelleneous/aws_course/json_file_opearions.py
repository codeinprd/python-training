import json

input_file="example_json_file.json"

f = open(input_file,"r")

records = json.load(f)

for item in records["data"]:
    print(item)

f_out = open("demo_output.json","w")
json.dump(records,f_out)



