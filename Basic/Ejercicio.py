class Fruit(object):

    def __init__(self):
       print("This is the instance of Fruit class.")

    def Nutrition(self):
        print("Taking your fruits. ")

    def Fruit_Shape(self):
        print("Shape: Round.")

Fr = Fruit()
Fr.Nutrition()
Fr.Fruit_Shape()

class Orange(Fruit):
    def __init__(self, Colorsito):
        #Fruit.__init__(self)
        self.Colorsito = Colorsito
        print("This is the instance of Orange class.")

    def Nutrition(self):
        print("Drinking your" , self.Colorsito," juice.")

    def Color(self):
        print("Color: ", self.Colorsito)

Or = Orange('Orange')
Or.Nutrition()
Or.Color()
Or.Fruit_Shape()