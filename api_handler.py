import logging
import logging.handlers

def getApiLogger(name, url = '/logger'):
    logger = logging.getLogger(name)
    logger.setLevel('WARNING')
    apiHandler = logging.handlers.HTTPHandler('localhost:5000', url, 'POST')
    logger.addHandler(apiHandler)

    return logger


a = getApiLogger('hola')

print(a)
print(a.handlers)
a.warning("Hola")