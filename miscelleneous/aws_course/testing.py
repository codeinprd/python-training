from collections import defaultdict
marks={
    "subjects": [
        {
            "math": [
                {
                    "ram": 85
                },
                {
                    "krishna": 90
                },
                {
                    "bhanu": 95
                }
            ]
        },
        {
            "physics": [
                {
                    "ram": 75
                },
                {
                    "krishna": 77
                },
                {
                    "bhanu": 79
                }
            ]
        },
        {
            "chemistry": [
                {
                    "ram": 61
                },
                {
                    "krishna": 65
                },
                {
                    "bhanu": 69
                }
            ]
        },
        {
            "computer_science": [
                {
                    "ram": 57
                },
                {
                    "krishna": 71
                },
                {
                    "bhanu": 42
                }
            ]
        },
        {
            "logical_reasoning": [
                {
                    "ram": 42
                },
                {
                    "krishna": 88
                },
                {
                    "bhanu": 68
                }
            ]
        }
    ]
}

dict_all = {}
for item in marks.get("subjects"):
    dict_all.update(item)


output_dict = { "RAM" : 0, "KRISHNA" : 0, "BHANU" : 0}
for value in dict_all.values():
    for mark in value:
        if "ram" in mark.keys():
            output_dict["RAM"] +=mark.get("ram")
        elif "krishna" in mark.keys():
            output_dict["KRISHNA"] +=mark.get("krishna")
        elif "bhanu" in mark.keys():
            output_dict["BHANU"] +=mark.get("bhanu")
print(output_dict)