import os
import zipfile
from datetime import datetime

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
