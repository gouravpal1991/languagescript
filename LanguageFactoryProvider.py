class LanguageFactoryProvider:
    def __init__(self, languageFactory=None):
        self.languageFactory = languageFactory

    def execute(self):
        platform = self.languageFactory()
        platform.generateDirectories()
        platform.writeToFile()
        