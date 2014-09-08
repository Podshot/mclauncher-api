import json
import urllib2
import urllib
import os
import sys

class MCLauncher(object):

    def __init__(self, version):
        self.version = version
        self.getVersionJSON()
    
    def getJar(self):
        urllib.urlretrieve(self.version.getJarURL(), self.version.getJarName())
        
    def downloadResources(self):
        return
    
    def getVersionJSON(self):
        self.version.getVersionJSON()
        
        