

class Car(object): #inherits from the 'object'class

    wheels = 4 #global, class variable, available to everybody, every method, may be modified on the instance not globally
    #IT IS NOT RECOMMENDED TO ACCESS THE MEMBER/GLOBAL VARIABLE THROUGH THE INSTANCE
    #DO IT THROUGH THE CLASS.MEMBER_VARIABLE

    def __init__(self, make, model="550"):
    # required method to initialize all the objs/attributes that are created on the class
    #constructor, self es como el this en java. Instance variables, they change with every instance, Car1, Car2, etc
        self.make = make
        self.model = model

    def Info(self):#using self as the param
        print("Model of the car: ", self.model)
        print("Make of the car: ", self.make)

Car1 = Car('Toyota') # instanciando la clase, creando obj,poniendo el parametro
print (Car1.make)
print (Car1.model)
Car1.wheels = 3 #modified the global variable on the instance of the class/object
print("NO  modifico las llantas, variable global, solo la instancia: ", Car1.wheels)

Car2 = Car('BMW') # instanciando la clase, creando obj,poniendo el parametro, C2 variable referencia de la instancia
print (Car2.make)
print (Car2.model)
print("Las llantas, variable global: ", Car.wheels)#printing the value of wheels global variable

#print("Variable global, FUERA DE LAS INSTANCIAS: ", Car.wheels)

Car3 = Car('Nissan') # instanciando la clase, creando obj,poniendo el parametro
print (Car3.make)
print (Car3.model)
Car.wheels = 3 #aqui si modifico la variable global
print("Si modifico las llantas, variable global: ", Car.wheels)

Car4 = Car("Acura", 'SF123')
Car4.Info()#using the method I created to print the info

print("Variable global, FUERA DE LAS INSTANCIAS: ", Car.wheels)