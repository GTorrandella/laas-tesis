import logging
import logging.handlers

def getRsyslogLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel('WARNING')
    syslogHandler = logging.handlers.SysLogHandler(address=('/dev/log'))
    logger.addHandler(syslogHandler)

    return logger


a = getRsyslogLogger('hola')

print(a)
print(a.handlers)
a.warning("Hola")