import os
import platform
from mclauncher.api.common import OS_API

class Macintosh(OS_API.OS):
    
    def __init__(self):
        self.WORKDIR = None
        
    def getDisplayName(self):
        return "MAC OS"

    def getMinecraftName(self):
        return "macos"

    def getArchitecture(self):
        return platform.architecture()[0]

    def getWorkingDirectory(self):
        if self.WORKDIR != None:
            return self.WORKDIR
        home = os.path.expanduser("~")
        if os.path.exists(home):
            if os.path.exists(home + "\Library/Application Support/.minecraft"):
                self.WORKDIR = home + "Library/Application Support/.minecraft"
    
        return self.WORKDIR
    
    def setWorkingDirectory(self, Wdir):
        self.WORKDIR = Wdir