
import logging

class LoggerDemoConsole():
    def testlog(self):


        #Create Logger - #Define Object name, variable name can be anything - Log record object
        #logger = logging.getLogger('Sample_Log')
        logger = logging.getLogger(LoggerDemoConsole.__name__)#to assign a more generic name(Class name)
        logger.setLevel(logging.INFO) #Just print INFO


        #Create console handler and set level to info
        chandler = logging.StreamHandler() #streamhandler is to write to the console
        chandler.setLevel(logging.INFO)#setting the level

        #Create formatter - Name is to add the name of where it is coming
        formatter = logging.Formatter('%(asctime)s: %(name)s, %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


        #Add formatter to console handler ->ch
        chandler.setFormatter(formatter) #assign it


        #Add console handler to logger
        logger.addHandler(chandler)

        #logging messages
        logger.debug('Debug Message')
        logger.info('Info Message')
        logger.info('Warn Message')
        logger.info('Error Message')
        logger.info('Critical Message')

Demo = LoggerDemoConsole()
Demo.testlog()