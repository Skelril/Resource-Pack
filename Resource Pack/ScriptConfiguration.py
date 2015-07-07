import os
import json
from Settings import *

print("This script will configure the Creation Script for you!")

settings = findOrInitSettings()

response = input("Would you like the script to automatically remove old files? [y/N] ")
settings.alwaysRemoveOld = response.lower() == "y"

response = input("Would you like the script to automatically create a copy of the generated texture pack in your resource pack's directory? [y/N] ")
settings.livePatching = response.lower() == "y"

if settings.livePatching:
    response = input("What would you like to name the generated resource pack? [blank for generated file name]\n")
    if len(response) > 0:
        settings.livePatchingPack = response

    response = input("What is the full path of your MineCraft directory?\n")
    settings.MCPackDirectory = response

saveSettings(settings)
