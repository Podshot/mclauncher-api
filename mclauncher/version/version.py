import urllib2
import json

'''
Minecraft Version container
'''
class Version(object):
    
    '''
    Initalizes a new Minecraft Version
    
    param: vid: The Minecraft Version name
    param: json: The <minecraft version>.json file parsed with python's built in json module
    '''
    def __init__(self, vid, json):
        self.id = vid
        self.type = json["type"]
        self.minimumLauncherVersion = json["minimumLauncherVersion"]
        self.minecraftArguments = json["minecraftArguments"]
        self.mainClass = json["mainClass"]
        self.libraries = json["libraries"]
        
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
    
    def getVersionJSON(self):
        site = urllib2.urlopen("http://s3.amazonaws.com/Minecraft.Download/versions/" + self.getID() + "/" + self.getID() + ".json").read()
        return json.loads(site)
    
    def getJarName(self):
        return self.getID() + ".jar"
    
    def getJarURL(self):
        return "https://s3.amazonaws.com/Minecraft.Download/versions/" + self.getID() + "/" + self.getID() + ".jar"