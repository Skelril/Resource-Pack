#
# Copyright (c) 2015 Wyatt Childers.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
import json
import shutil
import zipfile
from Settings import *
from datetime import datetime

settings = findOrInitSettings()

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

# Live patching

if settings.livePatching:
    newDir = settings.MCPackDirectory + '/' + settings.livePatchingPack

    shutil.rmtree(newDir, True)
    shutil.copytree('../Primary/assets', newDir + '/assets')
    shutil.copyfile('./Dependencies/pack.mcmeta', newDir + '/pack.mcmeta')
    print("File copied to your resource pack directory!")

# Old file removal

removeOld = False
if settings.alwaysRemoveOld:
    removeOld = True
else:
    clearFiles = input("Remove old resource packs? [y/N] ")
    if clearFiles.lower() == 'y':
        removeOld = True

if removeOld:
    for file in os.listdir():
        if file == zipFilename:
            continue
        if re.match("Test Pack \(.*\)\.zip", file):
            os.remove(file)
            print(file + " removed!")
