import os
import json

print("This script will configure the Creation Script for you!")

response = input("Would you like the script to automatically remove old files? [y/N] ")
removeAlways = response.lower() == "y"

response = input("Would you like the script to automatically create a copy of the generated texture pack in your resource pack's directory? [y/N] ")
autoCopyEnabled = response.lower() == "y"

if autoCopyEnabled:
    response = input("What would you like the generated file to be called (in your resource pack directory)? [blank for generated file name]\n")
    autoCopyConstantName = response
    response = input("What is the full path of your MineCraft directory?\n")
    autoCopyResourceDirectory = response
else:
    autoCopyConstantName = "Skelril Test Pack.zip"
    autoCopyResourceDirectory = ""

open("custom-settings.json", 'w').write(
    json.dumps(
        {
            "removal" : {
                "always" : removeAlways
            },
            "auto copy" : {
                "enabled" : autoCopyEnabled,
                "constant name" : autoCopyConstantName,
                "resource pack directory" : autoCopyResourceDirectory
            }
        }
    )
)
