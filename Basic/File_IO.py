"""
File I/O
'W' -> write only mode
'R' -> read only mode
'R+' -> read and write mode
'A' -> append mode
1.Open the file
2.Run through it with for
3.Close

"""
my_list = [5,6,7]

#my_file is the variable/name of the file object. Open() is the function to open the file
my_file = open("File_IO.txt", 'w')

for item in my_list:
    my_file.write(str(item)) #the write method uses a 'string' argument. Need to insert the item of the for.
    #the parameter has to be caster to an string, using str() function
    my_file.write(str(item) + "\n")# This  + "\n" will add the items in every line.
 #File needs to be closed. At this point python knows data has been written correctly.
my_file.close()

my_file2 = open("fileNew.txt", 'a') # 'a' mode will append it to the end of the file
word = '#*'*20
for item in word:
    my_file2.write(item + "\n")
my_file2.close()