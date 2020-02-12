#INHERITANCE

class Car2(object):
    def __init__(self):
        print('Hello there. Instance created')

    def drive(self):
        print('Engine started ... brrrm, brrrrm')

    def stop(self):
        print('Engine stopped ...')

Carrito = Car2()#Instanciando la clase padre
Carrito.drive()
Carrito.stop()

class BMW(Car2): # 'BMW es el nombre de la nueva clase y Car2 de donde hereda Clase HIJO(PADRE):'
    def __init__(self):
        #super().__init__() # this is a warning only, to call the init method of the superclass, it can be Father.__init__()
        print('BMW instance of the inherited class Car2')


InstanciaDeClaseHeredada = BMW() #Instanciando la clase heredada
InstanciaDeClaseHeredada.stop()
InstanciaDeClaseHeredada.drive()