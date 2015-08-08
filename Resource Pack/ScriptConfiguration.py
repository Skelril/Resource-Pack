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
