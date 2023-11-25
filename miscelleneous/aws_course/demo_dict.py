demo_dict = {
    "data" : [ "ram" , "krishna", "bhanu"]
}

#list_data = demo_dict.get("data")
# list_data = demo_dict["data"]

# for item in list_data:
#     print(item.upper())

demo_dict_2 = {
    "data" : [ 
        { "name" : "ram"},
        { "name" : "bhanu" },
        { "name" : "krishna" }
    ]
}

# output_list = demo_dict_2.get("data")
# for item in output_list:
#     print(item.get("name"))


# emp_data = {
#     "data" : [
#         {
#             "name" : "ram",
#             "salary" : 100
#         },
#         {
#             "name" : "krishna",
#             "salary" : 200
#         },
#         {
#             "name" : "Kunal",
#             "salary" : 500
#         }
#     ]
# }

# for emp in emp_data["data"]:
#     if emp["name"] == "Kunal":
#         print(emp["salary"])

# team_india = {
#     data = [
#         {"name" = "Virat",
#          "runs" = 120}
         
         
#         {"name" = "Dhoni",
#           "runs" = 100}

#         {'name" = "Pandya",
#            "runs" = 70}
#     ]
# }

# sub_dict={
#     "subjects": [
#         {
#             "math": [
#                 {
#                     "ram": 85
#                 },
#                 {
#                     "krishna": 90
#                 },
#                 {
#                     "bhanu": 95
#                 }
#             ]
#         },
#         {
#             "physics": [
#                 {
#                     "ram": 75
#                 },
#                 {
#                     "krishna": 77
#                 },
#                 {
#                     "bhanu": 79
#                 }
#             ]
#         },
#         {
#             "chemistry": [
#                 {
#                     "ram": 61
#                 },
#                 {
#                     "krishna": 65
#                 },
#                 {
#                     "bhanu": 69
#                 }
#             ]
#         }
#     ]
# }

# sub_list = sub_dict["subjects"]
# for item in sub_list:
#     # print(item.items())
#     # #marks_list = item[""]
#     for key,value in item.items():
#         print(key,value)
#         subject_name = key
#         subject_marks = value
#         subject_total=0
#         for mark in subject_marks:
#             subject_total=subject_total+list(mark.values())[0]

#         print(subject_total)


demo={
    "cricket": [
        {
            "batting_records": [
                {
                    "test_records": [
                        {
                            "most_runs": [
                                {
                                    "sachin": 15000
                                },
                                {
                                    "sangkara": 14000
                                },
                                {
                                    "Kallis": 13500
                                }
                            ]
                        },
                        {
                            "most_centuaries": [
                                {
                                    "sachin": 51
                                },
                                {
                                    "sangkara": 37
                                },
                                {
                                    "Kallis": 43
                                }
                            ]
                        }
                    ]
                },
                {
                    "odi_records": [
                        {
                            "most_runs": [
                                {
                                    "sachin": 18500
                                },
                                {
                                    "sangkara": 14200
                                },
                                {
                                    "Ponting": 13700
                                },
                                {
                                    "Kohli": 13400
                                }
                            ]
                        },
                        {
                            "most_centuaries": [
                                {
                                    "sachin": 49
                                },
                                {
                                    "kohli": 48
                                },
                                {
                                    "Rhoit": 31
                                },
                                {
                                    "Ponting": 30
                                }
                            ]
                        }
                    ]
                },
                {}
            ]
        },
        {
            "bowling_records": []
        }
    ]
}
#print(demo.get("cricket")[0].get("batting_records")[0].get("test_records")[0].get("most_runs")[0]["sachin"])