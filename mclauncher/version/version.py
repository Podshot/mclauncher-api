import urllib2
import json

class Version(object):

    def __init__(self, id, type):
        self.id = id
        self.type = type
        
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