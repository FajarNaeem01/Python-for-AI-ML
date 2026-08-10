"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 04 - JSON
Practice File

Author: Fajar Naeem Rana
===============================================
"""
import json
# dumps() and loads()
#=====================
student = {
    "name": "Fajar",
    "age": 20,
    "university": "QAU",
    "cgpa": 3.2
} 
json_string=json.dumps(student, indent=4, sort_keys=True)
print(json_string)
print(type(json_string))

json_data = '{"name": "Fajar", "age": 20, "cgpa": 3.2}'
python_object=json.loads(json_data)
print(python_object)
print(type(python_object))

# dump() and load()
# =======================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.json", "w") as file:
    json.dump(student, file, indent=4)

with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.json", "r") as file:
    loaded_data=json.load(file)
print(f"Type of loaded data: {type(loaded_data)}")
print(f"Loaded data:")
print(loaded_data)
          