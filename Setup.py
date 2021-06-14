import json
import sys

sys.setrecursionlimit(5000)


class Setup:
    __instance = None
    # location of the config file
    __configFileLocation = "configuration//config.json"

    # parsed config object
    __configObj = None

    @staticmethod
    def getInstance():
        """---static access method----"""
        if Setup.__instance == None:
            Setup()
        return Setup.__instance

    def __init__(self):
        """---virtually private constructor--- """
        if Setup.__instance != None:
            raise Exception("Setup class is singleton!")
        else:
            Setup.__instance = self

    def __parseConfigFile(self):
        # reading config file
        configFile = open(Setup.__configFileLocation, 'r')
        jsonData = configFile.read()
        # parse
        Setup.__instance.__configObj = json.loads(jsonData)
        return Setup.__instance.__configObj

    """---function to return default configuration for the script---"""
    @staticmethod
    def buildConfigurationObject():
        return Setup.__instance.__parseConfigFile()

  # function to get supported countries list
    @staticmethod
    def getContriesList():
        if Setup.__instance.__configObj != None:
            return Setup.__instance.__configObj["countries"]
        else:
            raise Exception("Config obj is not set")

    # function to get supported countries list
    @staticmethod
    def getLanguageDirectories():
        if Setup.__instance.__configObj != None:
            return Setup.__instance.__configObj["languageDirs"]
        else:
            raise Exception("Config obj is not set")

    # to get deault directory
    @staticmethod
    def getDefaultLangDir():
        if Setup.__instance.__configObj != None:
            return Setup.__instance.__configObj["languageDirectory"]
        else:
            raise Exception("Config obj is not set")

    # to get deault directory
    @staticmethod
    def getTemplateFileDirectories():
        if Setup.__instance.__configObj != None:
            return Setup.__instance.__configObj["templateFile"]
        else:
            raise Exception("Config obj is not set")
    
     # function to to get csv file data
    @staticmethod
    def getTranslationFile():
        if Setup.__instance.__configObj != None:
            return Setup.__instance.__configObj["csvFilePath"]
        else:
            raise Exception("Config obj is not set")

    # # function to get supported language specific directories name list
    # # e.g. android->values, ios->en.lproj/laguage.strings
    # @staticmethod
    # def getLanguageDirectories():
    #     if Setup.__instance.__configObj != None:
    #         return Setup.__instance.__configObj["languageDirs"]
    #     else:
    #         raise Exception("Config obj is not set")
