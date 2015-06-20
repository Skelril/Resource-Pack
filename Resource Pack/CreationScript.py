import os
import re
import json
import shutil
import zipfile
from datetime import datetime

class Settings:
    def __init__(self, json):
        self.alwaysRemoveOld = json['removal']['always']
        autoCopy = json['auto copy']
        self.autoCopyEnabled = autoCopy['enabled']
        self.autoCopyConstantName = autoCopy['constant name']
        self.autoCopyResourceDirectory = autoCopy['resource pack directory']

settings = Settings(json.load(open('script-settings.json')))

date = datetime.today()

zipFilename = "Test Pack (" + str(date.month) + "-" + str(date.day) + "-" + str(date.year) + "-" + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second) +").zip"

with zipfile.ZipFile(zipFilename, "w") as myzip:
    for dir, subdirs, files in os.walk("../Primary/assets"):
        assetsDir = dir.replace("../Primary/", "")
        myzip.write(dir, assetsDir)
        for filename in files:
            myzip.write(os.path.join(dir, filename), os.path.join(assetsDir, filename))

    myzip.write("./Dependencies/pack.mcmeta", "pack.mcmeta")
    myzip.close()

print("Resource pack generated successfully as '" + zipFilename + "'!")

# Auto copy

if settings.autoCopyEnabled:
    newFile = settings.autoCopyResourceDirectory + "/"
    if len(settings.autoCopyConstantName) > 0:
        newFile += settings.autoCopyConstantName
    else:
        newFile += zipFilename

    shutil.copyfile(zipFilename, newFile)
    print("File copied to your resource pack directory!")

# Old file removal

removeOld = False
if settings.alwaysRemoveOld:
    removeOld = True
else:
    clearFiles = input("Remove old resource packs? [y/N] ")
    if clearFiles.lower() == 'y':
        removedOld = True

if removeOld:
    for file in os.listdir():
        if file == zipFilename:
            continue
        if re.match("Test Pack \(.*\)\.zip", file):
            os.remove(file)
            print(file + " removed!")
