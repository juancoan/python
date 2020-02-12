#Errors
# We ensure through exceptions our code runs fine and without unwanted issues.
# https://docs.python.org/3/library/exceptions.html

def PruebaExcepcion():
    try: # On the try block you put whatever you will submit to the try or check
        a=3
        b=4
        c=0
        operacion = (a+b)/c
        print("La operacion da como resultado: ", operacion)
    except: #however you will handle the exception
        print("Division by cero is not allowed. ")

def PruebaExcepcionMultiple():
    try: # On the try block you put whatever you will submit to the try or check
        a=3
        b="Hello there. "
        c=0
        operacion = (a+b)/c
        print("La operacion da como resultado: ", operacion)
    except ZeroDivisionError: #however you will handle the exception, including a pre-existing exception
        print("Division by cero is not allowed. ")
    except TypeError: #however you will handle the exception, including a pre-existing exception
        print("Concatenating a string with int is not allowed. ")
PruebaExcepcion()
PruebaExcepcionMultiple()# On this one you will see the first exception that happens.