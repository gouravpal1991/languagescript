# importing os module
import os
# to remove directory
import shutil
import csv
from Setup import Setup
from LanguageFactory import AbstractLanguageFactory


class AndroidLanguageImplementation(AbstractLanguageFactory):

    __instance = None

    __tempLanguageFilepaths = []

    @staticmethod
    def getInstance():
        """---static access method----"""
        if AndroidLanguageImplementation.__instance == None:
            AndroidLanguageImplementation()
        return AndroidLanguageImplementation.__instance

    def __init__(self):
        """---virtually private constructor--- """
        if AndroidLanguageImplementation.__instance != None:
            raise Exception("Setup class is singleton!")
        else:
            AndroidLanguageImplementation.__instance = self

    def generateDirectories(self):
        print("-"*50 + "\nProcess started for generating android directories")
        print("-"*50)
        try:
            # creating android directory
            androidDirectoryPath = os.path.join(
                Setup.getDefaultLangDir(), "android")
            os.makedirs(androidDirectoryPath)

            # getting android platform details
            directories = Setup.getLanguageDirectories()
            platform = directories[1]

            # getting list of countries
            countryList = Setup.getContriesList()
            successCount = 0
            failureCount = 0
            for country in countryList:
                try:
                    # create values directory
                    countryDirectoryName = platform.get(
                        "name") + '-'+country.get("transDirAndroid")
                    # create directory path for country specific language
                    languageFilepath = os.path.join(
                        androidDirectoryPath, countryDirectoryName)

                    filePath = {
                        "languageCode": country.get("languageCode"),
                        "filePath": languageFilepath+'/'+platform.get("langFileName")
                    }
                    self.__tempLanguageFilepaths.append(filePath)
                    # generating directory for language
                    os.mkdir(languageFilepath)
                    # copy template file
                    shutil.copy2(platform.get(
                        "templateFilePath"), languageFilepath)
                    successCount += 1
                except:
                    print("Error while generating android directory for: " +
                          country.get("languageCode"))
                    failureCount += 1

            print("No of directories created: " + str(successCount))
            print("-"*50 + "\nDirectories successfully generated for android")
            print("-"*50)
        except:
            print("Error while generating the directories for android")

    def generateTemplateFiles(self):
        return super().generateTemplateFiles()

    def writeToFile(self):
        languageCodeMapping = []
        with open(Setup.getTranslationFile(), mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                for column in row:
                    valueOfColumn = ''
                    if line_count == 0:
                        obj = {
                            "index": row.index(column),
                            "value": column
                        }
                        languageCodeMapping.append(obj)
                        #TODO::
                    else:
                        print(f'{row}')
                line_count += 1
                print(f'{row}')

    def findElementInFile(self):
        return super().findElementInFile()

    def getTempFilePaths(self):
        print(self.__tempLanguageFilepaths)
