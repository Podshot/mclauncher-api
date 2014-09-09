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
        verJSON = json.loads(urllib2.urlopen('http://s3.amazonaws.com/Minecraft.Download/versions/' + mcVersion['id'] + '/' + mcVersion['id'] + '.json').read())
        ver = Version(mcVersion["id"], verJSON)
        versionDictionary[mcVersion["id"]] = ver
        
        print versionDictionary[mcVersion["id"]].getID()
        
def getVersions():
    return versionDictionary
    
    
startDownload()
