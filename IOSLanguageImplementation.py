from LanguageFactory import AbstractLanguageFactory


class IOSLanguageImplementation(AbstractLanguageFactory):

    def generateDirectories(self):
        print("In generateDirectories")
        return super().generateDirectories()

    def writeToFile(self):
        return super().writeToFile()

    def generateTemplateFiles(self):
        return super().generateTemplateFiles()

    def findElementInFile(self):
        return super().findElementInFile()
