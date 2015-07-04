import os
import json

class Settings:
    def __init__(self, json = None):
        if json == None:
            self.alwaysRemoveOld = False;
            self.livePatching = False;
            self.livePatchingPack = "Skelril Test Pack"
            self.MCPackDirectory = ""
        else:
            self.alwaysRemoveOld = json['removal']['always']
            livePatching = json['live patching']
            self.livePatching = livePatching['enabled']
            self.livePatchingPack = livePatching['pack name']
            self.MCPackDirectory = livePatching['resource pack directory']

    def dump(self, file):
        open(file, 'w').write(
            json.dumps(
                {
                    'removal' : {
                        'always' : self.alwaysRemoveOld
                    },
                    'live patching' : {
                        'enabled' : self.livePatching,
                        'pack name' : self.livePatchingPack,
                        'resource pack directory' : self.MCPackDirectory
                    }
                }
            )
        )

def findOrInitSettings():
    if not os.path.isfile('custom-settings.json'):
        settings = Settings()
        settings.dump('custom-settings.json')
    else:
        settings = Settings(json.load(open('custom-settings.json')))

    return settings

def saveSettings(settings):
    settings.dump('custom-settings.json')
