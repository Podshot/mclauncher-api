import urllib2
import urllib
import json
from mclauncher.implementation.version.Version import Version


class MCDownloadVersionList(object):
    versionDictionary = {}
    
    def __init__(self):
        self.startDownload()
        return None
    
    def startDownload(self):
        jsonString = urllib2.urlopen("http://s3.amazonaws.com/Minecraft.Download/versions/versions.json").read()
        versionJSON = json.loads(jsonString)
        for mcVersion in versionJSON["versions"]:
            verJSON = json.loads(urllib2.urlopen('http://s3.amazonaws.com/Minecraft.Download/versions/' + mcVersion['id'] + '/' + mcVersion['id'] + '.json').read())
            ver = Version(mcVersion["id"], verJSON)
            self.versionDictionary[mcVersion["id"]] = ver
        
            print self.versionDictionary[mcVersion["id"]].getID()
        return
        
    def getVersions(self):
        return self.versionDictionary

'''
Prevents a double launch bug in PyDev, not to be used in API
'''
def getVersionList(): 
    return MCDownloadVersionList().getVersions()
    
#getVersionList()