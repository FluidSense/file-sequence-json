from os import listdir, walk, getcwd
from os.path import isfile, join
import json

def getSubFolders():
    f = []
    for (dirpath, dirnames, filenames) in walk(getcwd() + "/img/"):
        f.extend(dirnames)
        break
    return f

def getFileNames(folderName):
    f = []
    for (dirpath, dirnames, filenames) in walk(getcwd() + "/img/" + folderName):
        f.extend(filenames)
        break
    return f

def createJson(fileNames):
    data = {}
    prevFile = ""
    for filename in fileNames:
        thisObject = {"name": filename, "nextImg": "", "prevImg": ""}
        if prevFile and prevFile in data:
            data[prevFile]["nextImg"] = filename
            thisObject["prevImg"] = prevFile
        prevFile = filename
        data[filename] = thisObject
    return data

def saveDataToFile(folders):
    # Save a json file to each img folder
    for folder in folders:
        fileNames = getFileNames(folder)
        with open(join(getcwd(),"img",folder,"images.json"), "w+") as writeFile:
            json.dump(createJson(fileNames), writeFile)


saveDataToFile(getSubFolders())
