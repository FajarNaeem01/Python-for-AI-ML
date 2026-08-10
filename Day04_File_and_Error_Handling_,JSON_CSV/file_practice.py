"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 04 - File Handling
Practice File

Author: Fajar Naeem Rana
===============================================
"""
students=["Ali\n", "Ahmed\n", "Noor\n"]

# ==============================================
# 1. opening file using with, read(), write()
# ==============================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.txt", "w") as file:
    file.writelines(students)    # using writelines()

with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.txt", "r") as file:
    data= file.read()
print(data)

with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.txt", "r") as file:
    data=file.readline()          # using readline()
print(data)

with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.txt", "r") as file: 
    print(file.readlines())       # using readlines()

with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\student.txt", "r") as file:
    for line in file:             # iterating through file
        print(line)

# ==================================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\profile.txt", "w") as file:
    file.write("Name: Fajar")        # using multiple writes
    file.write("\nUniversity: QAU")
    file.write("\nMajor: Computer Science")
    file.write("\nGoal: AI/ML Engineer")

with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\profile.txt", "r") as file:
    data=file.read()
print(data)

# =================================================
# 2. Cursor position
# =================================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\profile.txt", "r") as file:
    print(file.tell())
    print(file.read(11))
    print(file.tell())
    file.seek(0)
    print(file.read())
    
