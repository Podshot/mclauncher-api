import urllib2
import json
from mclauncher.api.version import version_API

'''
Minecraft Version container
'''
class Version(version_API.Version):
    
    '''
    Initializes a new Minecraft Version
    
    param: vid: The Minecraft Version name
    param: json: The <minecraft version_API>.json file parsed with python's built in json module
    '''
    def __init__(self, vid, json):
        self.id = vid
        self.type = json["type"]
        self.minimumLauncherVersion = json["minimumLauncherVersion"]
        self.minecraftArguments = json["minecraftArguments"]
        self.mainClass = json["mainClass"]
        self.libraries = json["libraries"]
        if "assets" in json:
            self.assets = json["assets"]
        else:
            self.assets = "DEFAULT_ASSETS"
        
    def getMinecraftArguments(self):
        return self.minecraftArguments
    
    def getMinimumLauncherVersion(self):
        return self.minimumLauncherVersion
    
    def getMainClass(self):
        return self.mainClass
    
    def getLibraries(self):
        return self.libraries
        
    def getID(self):
        return self.id
    
    def getType(self):
        return self.type
    
    def getAssets(self):
        return self.assets
    
    def getVersionJSON(self):
        site = urllib2.urlopen("http://s3.amazonaws.com/Minecraft.Download/versions/" + self.getID() + "/" + self.getID() + ".json").read()
        return json.loads(site)
    
    def getJarName(self):
        return self.getID() + ".jar"
    
    def getJarURL(self):
        return "https://s3.amazonaws.com/Minecraft.Download/versions/" + self.getID() + "/" + self.getID() + ".jar"