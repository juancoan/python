import keyword
a = 'juan'
b = 'antonio'

print (a)
print (b)

c= 'no'
d = c
b = 'cordoba'
print (b)
print (c == d) # to check if it is  the same
print (c is d) # 2nd way to check if it is  the same

print (keyword.kwlist) #shows the list of keywords that are reserved

a = b = c = 13 #asigna un valor a varias variables
print (a)
print (b)
print (c)
print ('****************************************************************')
x, y, z = 13, 11, 1 #asigna valores a varias variables en 1 sola linea
print (x)
print (y)
print (z)

print ('****************************************************************')
int_num = 13
str_string = 'hola'
flt_float = 13.9

print (int_num)
print (str_string)
print (flt_float)

a = 10
b = 13
add = a+b+int_num
print ("Sum: ", add) #the comma , is used when printing info,

subst= b-a
print ("Substraction: ", subst)

mult= b*a
print ("Multiplication: ", mult)

div= b/a
print ("Division: ", div)

print ('****************************************************************')

#Emponentes
multi = 10 * 200 # multiplicacion normal
exp = 10 ** 2 # 10 elevedo a la 200

print ("Multiplicacion: ", multi, "Exponente: ",exp)

print ('****************************************************************')

#Residuo - Modulo
remainder1 = 10 % 3 # residuo
remainder2 = 10 % 2
print ("Remainder 10 % 3: ", remainder1, "Remainder 10 % 2: ",remainder2)

print ('****************************************************************')
#precendece, parenthesis have precendence over the rest, then */ and +
a = 10 + 2 * 5 / 15
b = (10 + 2) * 5 / 15
print (a)
print(b)

c = 10
c = c + 15
c += 15 #shorter way to  add values
print (c)
c -= 15 #shorter way to  add values
print (c)
c /= 15 #shorter way to  add values
print (c)
c *= 15 #shorter way to  add values
print (c)

print ('****************************************************************')
#booleans

t = True
f = False
print (t)
print (f)

print (bool(0)) # always be false
print (bool(11)) #true
print (bool(1))  #true
x = "" #empty string is false
print(bool(x))

x = "Something" #not empty string is true
print(bool(x))

print ('****************************************************************')
s = "Something"
ss = 'Something'
print(s)
print(ss)

s = 'Something with "double" quotes'
ss = "Something with 'simple' quotes"
sss = "Something with \"quotes\"" # the backslash will ignore the functionality of the quotes
print(s)
print(ss)
print(sss)
print ('****************************************************************')

#strings, index starts always with 0
first = 'ton'
print(first[0])
second = 'wen'[2]
print(second)

"""
methods
len() to check the length of the string
lower() to change the case of the letter
upper() to change the case of the letter
str()
"""
text = "Hello there from Juan"
print(text.lower()) #llama al metodo upper() dentro de la clase string para usarlo
print(text.upper())#llama al metodo upper() dentro de la clase string para usarlo
print(len(text))# recibe la variable como un parametro, saber la cantidad de letras o cantidad
print(text + str(2))
print("I want" + " " + "to concatenate" + " " + "some" + " " + "text")
print (first + " " + second)

A = "trulululalilolulu44lulu"
B = A.replace('lulu', 'JUAN',1)#REPLACE PARTS OF STRING, the count value is for the amount
# of instances, for example if there are 2 or more times where lulu appears
print(A)
print(B)

#sub strings
part = A[1:6]# I am using an index to point which areas to take, from the index 1 to 5.
# The 1st number is inclusive and the 2nd is NOT inclusive.
part2 = A[1:7:2] #The 3rd value, in this case number 2, so it will step every 2
print(part)
print(part2)
print (A[:]) #EVERYTHING IS INCLUDED
print(A[1:]) #it will only start from the index 1, 2nd letter. First index is 0
print(A[-3]) # it will start from right to left
print(A[::-1])
print ('****************************************************************')
#string formatting
city = "juanco"
tag = "event"
print("Welcome to your " + city +" "+ tag)
print("Welcome to your %s %s" %(city, tag)) #the %s indicate a variable and at the end you specify
# them with %(variable1, variable 2, etc)
a = "one two three"
l = a.split() #putting the items of the string into a list
print(l)
a="test"
print(a[:2])

print ('****************************************************************')
# LISTS (mutable, that can be edited. Some of these objects like lists and dictionaries are mutable ,
# meaning you can change their content without changing their identity.
# Other objects like integers, floats, strings and tuples are objects that can not be changed.)
car_models = ['audi', 'bmw', 'tesla']
empty_list = []
print (car_models)
print(empty_list)
print("#*"*20)
print(car_models[0]) #accessing the 1st element on the list.
print("#*"*20)
nums = [3, 9, 15]
sum = nums[1] + nums[2] #sum of the values using the index.
print(sum)

newcar_models = ['toyota', 'jac', 'tesla']
newcar_models[1] = 'niva' #replacing the index 1 with new value.
print(newcar_models)

print("List length: " , len(newcar_models))
newcar_models.append('Juan') #to add to the end of the list a new value
print(newcar_models)
newcar_models.insert(1, "Biuick") #to insert it on a position or index
print(newcar_models)

x=newcar_models.index('Juan') #to find the index of a value on a list, if there are 2, it wil provide the first one.
print ("The index of Juan is: ", x)

y = newcar_models.pop() #this will remove the las item on the list
print(y)
print(newcar_models)

newcar_models.remove('niva')#explicitly say what to remove
print(newcar_models)

slicing = newcar_models[0:2] #the first value is inclusive and the 2nd one is not, extracting those values
print(slicing)
b = newcar_models[2:] #till the end of the list
print(b)

print("#*"*20)
newcar_models.sort()#sorting the list.
print(newcar_models)
Tesla_Count = newcar_models.count('tesla')#method to count the number of times an element shows on the list
print(Tesla_Count)

print('*******************************************************')

l=[1, 2, 3, 3, 2, 1]
print(l[4:])
print(l[-2:])
print(l[4:6])
print(l[2:6])

print('*******************************************************')
#DICTIONARIES, it also has methods
#key:value pairs d={'k1':'v1','k2':'v2'} just mapping, no secuence, no index

cars= {'make':'BMW', 'model':'750e','year':'2020'}
print(cars) #print the dict
print(cars['model']) #to print the value corresponding to the key
print(cars['year'])
print("#*"*20)
year = cars['year']
print(year) #another way to show info
print("#*"*20)

d={}#empty dict
print(d)
d['key'] = 'A' #adding values
d['key-2'] = 'B' #adding values
d['key-3'] = 4
d['key-4'] = -2
print(d)
print("#*"*20)
sumario = d['key-3'] + d['key-4']
print(sumario)
sumario2 = d['key-3'] - d['key-4']
print(sumario2)
d['key-4']= sumario2
print(d)
print(d.values())
print(d.keys())
print(d.items())

print('*******************************************************')
# NESTED DICTIONARIES
#key:value pairs d={'k1':{'nestk1':'nestv1','nestk2':'v2'}} just mapping, no secuence, no index

carros={'MECHE':{'modelo':'E300','AñO':'2019'}, 'AUDI':{'modelo':'Q7','AñO':'2017'}}
print(carros)
print(carros['MECHE'])
print(carros['MECHE']['modelo'])
print(carros['AUDI'])

print("#*"*20)
#Nested dict methods, values, keys, all the items
print(carros.keys())
print(carros.values())
print(carros.items())
print("#*"*20)
carritos = carros.copy()#hacer una copia del dict
print(carritos)
carritos.clear()#hacer una limpia del dict
print(carritos)
print("#*"*20)
d={"key1":[1,2,3], "key2":[4,5,6], "key3":[7,8,9]}
value = d["key1"][2] #that #2 is th index on that list.
print(value)

print('*******************************************************')
#TUPLES, NOT MUTABLE, CAN'T MODIFY. List with [] square brackets, tuple with round parent.
#my_tuple[0] = 8 it will not work.
list = [4,5,6]
print(list)
list[2] = 9
print(list)
print("#*"*20)
my_tuple = (8,9,10,0,5,6,4,10)
print(my_tuple)
print(my_tuple[2])
print(my_tuple[1:])
print(my_tuple.index(10))
print(my_tuple.count(10))
print('*******************************************************')
#Boolean Comparators, it will return true or false
 # == value equality
 # != not equal to
 # < less than
 # > greater than
 # => or <=

bool_one = 10 == 10
bool_two = 10 == 0
not_equal = 10 != 10
less_than = 10 < 3
greater_than = 10 > 5
gt_eq = 10 <= 11
less_eq = 1 >= 2

print(bool_one)
print (bool_two)
print(not_equal)
print(less_than)
print(greater_than)
print(gt_eq)
print(less_eq)

print("#*"*20)
#Boolean Operators
"""
AND
True and True = True
True and False = False
False and False = False

OR
True or True = True
True or False = True
False or False = False

NOT
not True = False
not False = True

"""
print("#*"*20)
and_output1 = (10 == 10) and (10>9)
and_output2 = (10 == 10) and (10<9)
and_output3 = (10 != 10) and (10<9)
print (and_output1)
print (and_output2)
print (and_output3)
print("#*"*20)
or_output1 = (10 == 10) or (10>9)
or_output2 = (10 == 10) or (10<9)
or_output3 = (10 != 10) or (10<9)
print (or_output1)
print (or_output2)
print (or_output3)
print("#*"*20)
not_true = not(and_output1)
not_false = not(and_output3)
print(not_true)
print(not_false)
print("#*"*20)

#'Not' is evaluated first, then 'and' finally 'or'
bool_precedence = True or not False and False
print (bool_precedence)
print("#*"*20)
bool_precedence = 10 == 10 or not 5>5 and 8<1
print (bool_precedence)
print("#*"*20)
print('*******************************************************')
#Condittional
if 100 > 10:
    print("Hundred is greater than 10")

value = 'culo'

if value == 'green':
    print("Go")
elif value == 'yellow':
    print("Prepare to stop")
else:
    print("Stop")

print("It will always print")


print('*******************************************************')
"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

x = 0
while x < 10:
    #print("Value of x is: " + str(x))
    print("Value of x is: ", x)
    x = x + 1

l = []
num = 0
while num <= 25:
    l.append(num)
    print("Value of num is: " + str(num))
    num += 2.5

print(l)

print('*******************************************************')
"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 8:
        break
    print("This example is awesome")
    print("*"*20)
else:
    print("Just broke out of the loop")

# x = 0
# while x < 10:
#     print("Value of x is: " + str(x))
#     x = x + 1
#
#     if x == 8:
#         continue
#     print("This example is awesome")
#     print("*"*20)
#
# print("Just broke out of the loop")
print("#*"*20)
print('*******************************************************')
"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""
Rango = range(0, 20) #starting point and last number is exclusive, 3rd value will be the step
print(type(Rango))
print(Rango)

print("#*"*20)
print(*range(1, 11)) # 1 line to show the content of the range values
print("#*"*20)

l = [1, 2, 3]
for num in range(1, 4):
    print(num)

print("#*"*20)

print('*******************************************************')
#FOR loop

#recorriendo el string
my_string = "Juansito"
for letters in my_string:
    #print(letters)
    print(letters, end='')
print("")

#recorriendo el string
my_string = "Franchesquin"
for letters in my_string:
    if letters =='n':
       print(letters.upper(), end='')
    else:
       print(letters, end='')
print()
print("#*"*20)
lista = ['daihatsu', 'toyota', 'subaru', 'niva']
for carros in lista:
    print(carros)

numeritos = [9,5,66,34,46,76]
for nums in numeritos:
    print(nums*1.36)

print()
print("#*"*20)
my_dict = {'one': 1, 'eight': 8, 'six': 6,'eleven': 11,'twenty': 20}

for key in my_dict:
    #print(key)#will just print the key
    print("Dictionary 'key:value' pair: ",key, my_dict[key])# will print all the dic info
    #first I run through the keys, then print the value.
print("#*"*20)
for k in my_dict:
    if k == 'eight':
        print("BASURA")
    elif k == 'twenty':
        print("EXITO")
    else:
        print("CUALQUIERA")
print("#*"*20)
for k,v in my_dict.items(): #para recorrer los items dentro del dic, list, tuple, etc
    print(k)
    print(v)
print("#*" * 20)
print('*******************************************************')
#ITERATING OVER MULTIPLE LISTS
#This will show the items of the shorter ist.

list_A = [4,6,8,12,14,16,18,20]
list_B = [5,7,9,11,13,15,17]

for A,B in zip(list_A,list_B): #Will print both lists in pairs
    print(A, end=" ")
    print(B, end=" ")
print()
print()
for C,D in zip(list_A,list_B): #it will only compare to the shortest list, if they have different sizes
    if C>D:
        print(C, end=" ")
    else:
        print(D, end=" ")

print()
print('*******************************************************')
#METHODS

def prueba():
    print("This is a test method")
prueba() #calling the methods
print("#*"*20)

def pruebaSuma(n1, n2):
    suma = n1+n2
    print("This is the sum of",n1, "+", n2,": ",suma)

pruebaSuma(3,10) #calling the methods
pruebaSuma(-5,9)
print("#*"*20)

#RETURN STATEMENT
def anotherMethod(n3,n4):
    #resta = n3-n4
    #print(resta)
    return n3-n4 #returning the result of this

resta1 = anotherMethod(87,0) #storing the returned result on a variable
resta2 = anotherMethod(-24,9)

print(resta1) #printing the result
print(resta2)
print("#*"*20)

def Cities(city):
    CityList = ['San Jose', 'Heredia', 'Cartago', 'Alajuela', 'Puntarenas', 'Guanacaste','Limon']
    if city in CityList: #if it exists in the list
        #print("YEY!!! You found it")
        return True
    else:
        #print("Keep trying")
        return False

pregunta1 = Cities('Heredia')
pregunta2 = Cities('Sabanilla')
print(pregunta1)
print(pregunta2)

print("#*"*20)
#POSITIONAL = ARE LIKE OPTIONAL PARAMETERS
#positional are using the position

def pruebaSuma2(n1=5, n2=13):#This will be optional. Will be excuted if the ones below line 564 are not present
    suma = n1+n2
    print("This is the sum of",n1, "+", n2,": ",suma)

pruebaSuma2(3,10) #calling the methods
pruebaSuma2(-5,9)
print("#*"*20)

def pruebaSuma3(n1=5, n2=13):#This will be optional. Will be excuted if the ones below line 564 are not present
    suma = n1+n2
    print("This is the sum of",n1, "+", n2,": ",suma)

pruebaSuma3() #calling the methods without parameters will use the optional ones above. Line 560
#same as with return statement
print("#*"*20)
print('*******************************************************')
print("#*"*20)
#VARIABLE SCOPE
a = 11 #global variable

def test(a): #this is a local method variable
    print("The value of local a is: ", a)
    a = 3
    print("The new value of local a is: ", a)

print("The value of the global variable a is: ", a)
test(5)#calling the method with the parameter and local variable
print("#*"*20)
print("#*"*20)
#USING THE GLOBAL VARIABLE WITHOUT CHANGING IT
a = 11 #global variable
def testB(a): #this is a local method variable
    print("The value of local a is: ", a)
    a = 3
    print("The new value of local a is: ", a)

print("The global variable at the beginning: ", a)
testB(a)#calling the method with global variable as the parameter and seeing if it changes.
print("Did the global variable change? once it was used at the beginning: ", a)

print("#*"*20)
print("#*"*20)
#USING THE GLOBAL VARIABLE TO MODIFY IT
a = 15 #global variable
def testC(): #this is a local method variable
    global a #declare the variable as global on the place where I am using it, remove the parameter in
    # the parenthesis.
    print("The value of global 'a' is: ", a)
    a = 20
    print("The new value of global 'a' is: ", a)

print("The global variable at the beginning: ", a)
testC()#calling the method with global variable INSIDE THE METHOD and seeing if it changes.
print("Did the global variable change? once it was used at the beginning: ", a)

print('*******************************************************')
print("#*"*20)
#more functions
"""
max() take any number of args, returns the largest one
min() take any number of args, returns the smallest one
abs() Returns the absolute value, distance from 0, 1 parameter, positive values are returned
type() Return type of data it receives as an argument
"""
def Ops(*args): # the * symbol means that it can take any number of arguments
    print("Max :", max(args))#use the arguments I will pass on the method call
    print("Min :", min(args))
    print("Abs :", abs(5))
    print("Type of '99': ", type(99))
    print("Type of '9.99': ", type(9.99))
    print("Type of 'Hello': ", type("Hello"))
    Lista = [7,8,9]
    TupleX = (9,15,12,17)
    print("Type of 'Lista = [7,8,9]': ", type(Lista))
    print("Type of 'TupleX = (9,15,12,17)': ", type(TupleX))
Ops(3,-5,0,8,9,7,21,44)
print('*******************************************************')
print("#*"*20)
#CLASSES
#evertyhing is an object (properties/attributes)
# car obj, has color, model, year, make
#methods, like start engine, stop engine, brake - actions, operations





print("#*"*20)
print('*******************************************************')
print("#*"*20)
print('*******************************************************')

print("#*"*20)
print('*******************************************************')
print("#*"*20)

print('*******************************************************')

print("#*"*20)
print('*******************************************************')

print("#*"*20)
print('*******************************************************')

print("#*"*20)
print('*******************************************************')
print("#*"*20)

print('*******************************************************')
print("#*"*20)

print('*******************************************************')

print("#*"*20)
print('*******************************************************')