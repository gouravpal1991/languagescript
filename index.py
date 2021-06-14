from AndroidLanguageImplementation import AndroidLanguageImplementation
from LanguageFactoryProvider import LanguageFactoryProvider
from IOSLanguageImplementation import IOSLanguageImplementation
from Setup import Setup 
from LanguageDirectorySetup import LanguageDirectorySetup

obj = LanguageDirectorySetup()

obj.generateLanguageDirectories()

impl = IOSLanguageImplementation()
impl.generateDirectories()


platform = LanguageFactoryProvider(AndroidLanguageImplementation)
platform.execute()
