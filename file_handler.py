import logging
import logging.handlers

def getFileLogger(name, file = 'log.txt'):
    logger = logging.getLogger(name)
    logger.setLevel('WARNING')
    fileHandler = logging.FileHandler(file, encoding='utf-8')
    logger.addHandler(fileHandler)

    return logger


a = getFileLogger('hola')

print(a)
print(a.handlers)
a.warning("Hola")