"""
WITH  / AS keywords
"""

# print("Normal WRITE start")
# File2 = open("File_IO.txt", "w")
# File2.write("Trying to write to the file2.")
# File2.close() #If I do not write the close() statement, nothing will happen. ALWAYS write it
#
# print("Normal READ start")
# File3 = open("File_IO.txt", "r")
# for line in File3:
#     print(line)

print("WITH AS WRITE start")  #no need to use CLOSE statement
with open("WtihASDemo.txt", 'w') as VariableName: #start using 'with' keybord, variable object at the end 'as Variable name'
    print("Writting to file...")
    VariableName.write("Writting with WITH_AS function.") # same write function


print('#*'*20)

print("WITH AS READ start")  #no need to use CLOSE statement
with open("WtihASDemo.txt", 'r') as VariableName2:
    for lines in VariableName2:
        print(lines)

print('#*'*20)

print("Using .READ() function")  #no need to use CLOSE statement
with open("WtihASDemo.txt", 'r') as VariableName2:
    print(VariableName2.read())