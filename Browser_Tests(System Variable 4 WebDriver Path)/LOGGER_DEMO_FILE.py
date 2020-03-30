
import logging
import logging.config #this is to load the configuration file.

class LoggerDemoFile():
    def testlog(self):
        #Create Logger - #Define the file where the log will be saved. "XYZ.conf is the extension"
        logging.config.fileConfig('Logging_File.conf')#to assign a more generic name(Class name)
        logger = logging.getLogger(LoggerDemoFile.__name__)  # to assign a more generic name(Class name)
        logger.setLevel(logging.INFO) #Just print INFO

        #logging messages
        logger.debug('Debug Message')
        logger.info('Info Message')
        logger.info('Warn Message')
        logger.info('Error Message')
        logger.info('Critical Message')

Demo = LoggerDemoFile()
Demo.testlog()

#ALWAYS check the IMPORT statements
#ALSO CHECK THE CONFIG FILE where is pulls the config info
#on the CONFIG FILE (Logging_File.conf) on the line that has "args" if after the "," you write 'w'
#it will create a new file, if you leave it with 'a' it will append to the one already created.