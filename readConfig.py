import curses
import json

class ConfigObj:
    def __init__(self, fileName):
        try:
            configFile = open(fileName, "r")
            self.configData = configFile.read()
            configJson = json.loads(self.configData)
            self.url = configJson["url"]
            self.fanChangeeTemp = configJson["fanChangeTemp"]
            self.fanDelta = configJson["fanDelta"]
            self.voltageTrigger = configJson["voltageTrigger"]
            self.alpha = configJson["alpha"]
            self.modMin = configJson["modMin"]
            self.modSec = configJson["modSec"]
            self.exception = None
        except Exception, ex:
            self.exception = ex

