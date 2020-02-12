#ELSE on the exceptions is happening when no exceptions are present
# FINALLY is ALWAYS executed


def PruebaExcepcion():
    try: # On the try block you put whatever you will submit to the try or check
        a=3
        b=4
        c=0
        operacion = (a+b)/c
        print("La operacion da como resultado: ", operacion)
    except: #however you will handle the exception
        print("Division by cero is not allowed. ")
        raise Exception("Raise exception on another method raised by this one. ")
    #Raise Exception("MSGE") is to trigger the exception caused by this method being called/used on another place.
    else: #if there was no exception this would've executed.
        print("No exceptions happened, ELSE block is executed.")
    finally: #ALWAYS executed.
        print("FINALLY always is executed.")

PruebaExcepcion()