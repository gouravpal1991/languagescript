
# importing os module
import os
# to remove directory
import shutil
# for handling json files
import json
import csv
# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET


'''extraction configuration values from config'''
# parent_directory
print('Getting Parent Directory')
currentDirectory = os.getcwd()

# getting template paths
androidTemplateFilePath = "template//android//strings.xml"
# TODO::change template with ios langauge template
iosTemplateFilePath = "template//ios//strings.xml"

# temporary file for storing new files path
tempFilePathJSON = "configuration//tempFilePath.json"

# read file
print('Reading config file')
configFile = open('configuration//config.json', 'r')
jsonData = configFile.read()


# parse
print('Parsing config data')
configObj = json.loads(jsonData)

# getting countries list
countryList = configObj["countries"]

# getting default directories
directories = configObj["dir"]

# ios default directory name from config
print('Getting ios default directory name')
iosDirectory = directories[0].get("name")

# android default directory name from config
print('Getting android default directory name')
androidDirectory = directories[1].get("name")

# deleting existing language directory
languageDirectory = "language"
langDirPath = os.path.join(currentDirectory,
                           languageDirectory)
shutil.rmtree(langDirPath, ignore_errors=True)


# generating ios directory
iosDirectoryPath = os.path.join(langDirPath, "ios")
os.makedirs(iosDirectoryPath)
# adding android directory
androidDirectoryPath = os.path.join(langDirPath, "android")
os.makedirs(androidDirectoryPath)
# os.mkdir(androidPath)

# this will be used to store the file path for specific language
tempLanguageFilepaths = {
    "android": [],
    "ios": []
}

print('Creating language specific directories and files for Android and iOS')
for i in range(len(countryList)):
    # generate language specific directory for android and ios
    for j in range(len(directories)):
        countryDirectoryName = ''
        languageFilepath = ''
        tempFilePath = ''
        languageFileName = directories[j].get("langFileName")
        if directories[j].get("platform") == "android":
            # create values directory
            countryDirectoryName = directories[j].get(
                "name") + '-'+countryList[i].get("transDirAndroid")
            # create directory path for country specific language
            languageFilepath = os.path.join(
                androidDirectoryPath, countryDirectoryName)
            tempFilePath = androidTemplateFilePath

            filePath = {
                "languageCode": countryList[i].get("languageCode"),
                "filePath": languageFilepath+'/'+languageFileName
            }
            tempLanguageFilepaths["android"].append(filePath)
        else:
            countryDirectoryName = directories[j].get(
                "name") + '-'+countryList[i].get("transDirIos")
            languageFilepath = os.path.join(
                iosDirectoryPath, countryDirectoryName)
            tempFilePath = iosTemplateFilePath
            filePath = {
                "languageCode": countryList[i].get("languageCode"),
                "filePath": languageFilepath+'/'+languageFileName
            }
            tempLanguageFilepaths["ios"].append(filePath)
        # generating directory for language
        os.mkdir(languageFilepath)
        # copy template file
        shutil.copy2(tempFilePath, languageFilepath)


with open(tempFilePathJSON, "w") as outfile:
    json.dump(tempLanguageFilepaths, outfile)

print('-'*40)
print('Language specific folders and files are generated')
print('-'*40)


# csv file reading starts from here
tree = ET.parse(
    '//Users//gouravpal//Documents//Python//Python-csv//template//android//strings.xml')

listOfFilePath = ''
with open(tempFilePathJSON, 'r') as j:
    listOfFilePath = json.loads(j.read())

# getting file paths for ios
iosFilePaths = listOfFilePath["ios"]
print(iosFilePaths)
# getting file paths for android
androidFilePaths = listOfFilePath["android"]
print(androidFilePaths)

languageCodeMapping = []

with open('file.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    valueOfColumn = ''
    platformFilePath = ''

    for row in csv_reader:
        for column in row:
            valueOfColumn = ''
            if line_count == 0:
                obj = {
                    "index": row.index(column),
                    "value": column
                }
                languageCodeMapping.append(obj)
            else:
                valueOfColumn = next(
                    (x for x in languageCodeMapping if x["index"] == row.index(column)), None)

                if(valueOfColumn != ''):
                    # looping through the platforms android and ios
                    for i in range(len(directories)):
                        if directories[i].get("platform") == "android":
                            platformFilePath = next(
                                (x for x in androidFilePaths if x["languageCode"] == valueOfColumn["value"]), None)

                        else:
                            platformFilePath = next(
                                (x for x in iosFilePaths if x["languageCode"] == valueOfColumn["value"]), None)

                        if(platformFilePath != None):
                            location = platformFilePath["filePath"]
                            # writing into the language specific file
                            data = ET.Element('resources')
                            # Adding a subtag named `Opening`
                            # inside our root tag
                            element1 = ET.SubElement(data, 'string')
                            element1.set('name', row[0])
                            element1.text = row[valueOfColumn["index"]]
                            # Converting the xml data to byte object,
                            # for allowing flushing data to file
                            # stream
                            b_xml = ET.tostring(data)
                            # Opening a file with the auto generated location,
                            # with operation mode `wb` (write + binary)
                            with open(location, "wb") as f:
                                f.write(b_xml)

        line_count += 1
    print(f'Processed {line_count} lines.')
