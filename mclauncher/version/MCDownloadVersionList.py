import urllib2
import urllib
import json
from mclauncher.version.version import Version

versionDictionary = {}

def startDownload():
    jsonString = urllib2.urlopen("http://s3.amazonaws.com/Minecraft.Download/versions/versions.json").read()
    versionJSON = json.loads(jsonString)
    for mcVersion in versionJSON["versions"]:
        print mcVersion
        ver = Version(mcVersion["id"], mcVersion["type"])
        versionDictionary[mcVersion["id"]] = ver
        
        print versionDictionary[mcVersion["id"]].getID()
        
def getVersions():
    return versionDictionary
    
    
startDownload()
