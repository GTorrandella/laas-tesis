'''
Created on Sep 19, 2020

@author: Gabriel Torrandella
'''
from rejson import Client, Path

class Connector():
    
    def __init__(self):
        self._rj = Client(host='localhost', port=6379, decode_responses=True)

    def saveLog(self, logJson, logId):
        print("saveLog")
        self._rj.jsonset(logId, Path.rootPath(), logJson)

    def getLog(self, logId):
        return self._rj.jsonget(logId, Path.rootPath())