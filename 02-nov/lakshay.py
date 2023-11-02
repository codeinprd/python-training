records = demo_dict = {
    "subjects": [
        {"math": [{"ram": 85}, {"krishna": 90}, {"bhanu": 95}]},
        {"physics": [{"ram": 75}, {"krishna": 77}, {"bhanu": 79}]},
        {"chemistry": [{"ram": 61}, {"krishna": 65}, {"bhanu": 69}]},
        {"computer_science": [{"ram": 57}, {"krishna": 71}, {"bhanu": 42}]},
        {"logical_reasoning": [{"ram": 42}, {"krishna": 88}, {"bhanu": 68}]},
    ],
}


math_sum_marks, physics_sum_marks, chem_sum_marks, cs_sum_marks, lr_sum_marks = (
    0,
    0,
    0,
    0,
    0,
)

for rec in records.get("subjects"):#[{"math": [], "physics": []}]
    for subject, values in rec.items():#subject = math, values = [{"ram": 4, "krishna": 4,}]
        if subject == "math":
            for name in values:#name = {"ram"}
                for marks in name.values():
                    math_sum_marks += marks
        if subject == "physics":
            for name in values:
                for marks in name.values():
                    physics_sum_marks += marks
        if subject == "chemistry":
            for name in values:
                for marks in name.values():
                    chem_sum_marks += marks
        if subject == "computer_science":
            for name in values:
                for marks in name.values():
                    cs_sum_marks += marks
        if subject == "logical_reasoning":
            for name in values:
                for marks in name.values():
                    lr_sum_marks += marks

math_avg_marks = math_sum_marks / 3
physics_avg_marks = physics_sum_marks / 3
chem_avg_marks = chem_sum_marks / 3
cs_avg_marks = cs_sum_marks / 3
lr_avg_marks = lr_sum_marks / 3

print(math_avg_marks, physics_avg_marks, chem_avg_marks, cs_avg_marks, lr_avg_marks)

print(f"Average marks in maths is {lr_avg_marks}")
print(f"Average marks in physics is {math_avg_marks}")
print(f"Average marks in chemistry is {physics_avg_marks}")
print(f"Average marks in computer_science is {chem_avg_marks}")
print(f"Average marks in logical_reasoning is {cs_avg_marks}")
