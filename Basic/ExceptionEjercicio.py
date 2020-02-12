
class PruebaExcepcion():
    def Ejercicio(self):
        try:
            diction = {"Make": "Nissan", "Model":"Maxima", "Year": "2020"}
            print(diction['Make'])
            print(diction['Color'])
        except:
            print("Calling the wrong key.")
        finally:
            print("Remember to look for the correct key:value pair.")

Pr = PruebaExcepcion()
Pr.Ejercicio()