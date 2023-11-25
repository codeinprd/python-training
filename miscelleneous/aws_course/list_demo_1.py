salary = [ "$100", "$200", "$1200","#3200","#2500", "2399","3456"]
output_list = []

for item in salary:
    if "$" in item:
        item_formated = int(item.split("$")[1])
        print(item_formated)
        output_list.append(item_formated)
    elif "#" in item:
        item_formated = int(item.split("#")[1])
        print(item_formated)
        output_list.append(item_formated)
    else:
        item_formated = int(item)
        print(item_formated)
        output_list.append(item_formated)


print(output_list)
print(sum(output_list))