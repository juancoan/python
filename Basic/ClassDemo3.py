#METHOD OVERRIDING

class Car2(object):
    def __init__(self):
        print('Hello there. Instance created')

    def drive(self):
        print('Engine started ... brrrm, brrrrm')

    def Brake(self):
        print('Pressing the brake... Slowering speed...')

    def stop(self):
        print('Engine stopped ...')

Carrito = Car2()#Instanciando la clase padre
Carrito.drive()
Carrito.stop()
Carrito.Brake()

print("#*"*20)
print('*******************************************************')
class BMW(Car2): # 'BMW es el nombre de la nueva clase y Car2 de donde hereda Clase HIJO(PADRE):'
    def __init__(self):
        print('BMW instance of the inherited class Car2')

    def drive(self):
        print('Method override, you are driving a BMW')
        #TO OVERRIDE THE ORIGINAL RIDE METHOD, JUST CALL IT WITHIN THE CHILD CLASS AND WRITE INSITE IT

    def Brake(self):
        super().Brake()  # call the Brake method from the parent/super class and add functonality and override it.
        print("Overriding the Brake method and adding functionality.")
    # TO OVERRIDE THE ORIGINAL RIDE METHOD, JUST CALL IT WITHIN THE CHILD CLASS AND WRITE INSIDE IT
    # AND ADD FUNCTIONALTITY.

    def headup_display(self):
        print('This is an unique feature. ENJOY!')


InstanciaDeClaseHeredada = BMW() #Instanciando la clase heredada
InstanciaDeClaseHeredada.drive()
InstanciaDeClaseHeredada.stop()
InstanciaDeClaseHeredada.headup_display()
InstanciaDeClaseHeredada.Brake()
