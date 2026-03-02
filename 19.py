##
my_stu_dict = {
    "name": "spoo",
    "age": 19,
    "branch": "csbs"
}
print(my_stu_dict["name"])
print(my_stu_dict["age"])
print(my_stu_dict["branch"])

my_stu_dict["college"] = "malnad"
my_stu_dict["age"] = 20
print(my_stu_dict)

my_stu_dict.pop("age")
print("name" in my_stu_dict)
print(my_stu_dict.keys())
print(my_stu_dict.values())
