
import inspect
import logging


def testlog(logLevel): #takes the log level(info, debug, warning, etc) as param
        #Create Logger - Gets the name of the class/method from where this method is called.
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName) # to assign the name from the class that is gathered from inspect
        logger.setLevel(logging.DEBUG)#to log all messages

        #Create a file handler with the 'class name' obtained from the inspect
        fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
        fileHandler.setLevel(logLevel)

        # Create formatter - Name is to add the name of where it is coming
        formatter = logging.Formatter('%(asctime)s: %(name)s, %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # Add formatter to console handler ->ch
        fileHandler.setFormatter(formatter)  # assign it

        # Add console handler to logger
        logger.addHandler(fileHandler)

        return logger

