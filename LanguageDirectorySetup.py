from typing import Set
from Setup import Setup
# to remove directory
import shutil


class LanguageDirectorySetup:
    __configObj = None

    def __init__(self):
        LanguageDirectorySetup.__configObj = Setup.getInstance()
        LanguageDirectorySetup.__configObj.buildConfigurationObject()

    @staticmethod
    def generateLanguageDirectories():
        # getting countries list
        countryList = LanguageDirectorySetup.__configObj.getContriesList()

        # getting default directories
        directories = LanguageDirectorySetup.__configObj.getLanguageDirectories()

        # deleting existing language directory
        shutil.rmtree(
            LanguageDirectorySetup.__configObj.getDefaultLangDir(), ignore_errors=True)
