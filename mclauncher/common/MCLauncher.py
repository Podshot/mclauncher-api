import json
import urllib2
import urllib
import os
import sys

class MCLauncher(object):
    '''
    classdocs
    '''


    def __init__(self, version):
        self.version = version
    
    def getJar(self):
        urllib.urlretrieve(self.version.getJarURL(), self.version.getJarName())
        