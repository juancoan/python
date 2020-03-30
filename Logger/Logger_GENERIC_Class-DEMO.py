
import logging
import Code.Logger.Logger_GENERIC_Class as CL #import GENERIC class as an alias


class LoggingDemo():

        log = CL.testlog(logging.DEBUG) #calling the method from the other class, initialising & assigning a variable name

        def Method_1(self): #self.log used since it is pulling from the other class
                self.log.debug('Debug Message')
                self.log.info('Info Message')
                self.log.info('Warn Message')
                self.log.info('Error Message')
                self.log.info('Critical Message')

        def Method_2(self):
                NewFile=CL.testlog(logging.INFO) #Have this other method be logged on another file
                NewFile.debug('Debug Message')
                NewFile.info('Info Message')
                NewFile.info('Warn Message')
                NewFile.info('Error Message')
                NewFile.info('Critical Message')

        def Method_3(self):
                NewFile2 = CL.testlog(logging.CRITICAL)  # Have this other method be logged on another file
                NewFile2.debug('Debug Message')
                NewFile2.info('Info Message')
                NewFile2.info('Warn Message')
                NewFile2.info('Error Message')
                NewFile2.info('Critical Message')


Using_GenericMethod_Class = LoggingDemo()
Using_GenericMethod_Class.Method_1()
Using_GenericMethod_Class.Method_2()
Using_GenericMethod_Class.Method_3()
