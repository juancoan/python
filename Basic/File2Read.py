
my_file2 = open("File2Read.txt", 'r') #use the 'r' mode to read
print(str(my_file2.read())) #prints the read method, all the content of the file
my_file2.close()

print('#*'*20)

print("LINE BY LINE EXAMPLE......... Will print the first line only, unless I call that print method twice")
my_file_BY_LINE = open("File2Read.txt", 'r') #use the 'r' mode to read
print(str(my_file_BY_LINE.readline())) #prints the read method, all the content of the file
my_file_BY_LINE.close()

print('#*'*20)

print("LINE BY LINE EXAMPLE with FOR LOOP.........")
my_file_withFOR = open("File2Read.txt", 'r') #use the 'r' mode to read
for line in my_file_withFOR:
    Mayuscula = line.upper() #guardo el cambio en una variable y le aplico el metodo
    print(Mayuscula)#imprimo la variable
my_file_withFOR.close()