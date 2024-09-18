#Dictionaries are about (key : values) pairs

student = {"name": "krishna", "std": 5, "courses": ["Maths", "science"]}
student["name"]=("Ram")
print(student)
print(student.get("phone","not found"))#string that don't exists will response to none. 
student.update({"name": "Siya", "std": 3})
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

#For Loop example

for key in student:
    print(key)
for values in student.items():
    print(values)

for key, values in student.items():
    print(values)
