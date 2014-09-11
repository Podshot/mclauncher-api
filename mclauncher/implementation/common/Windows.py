import os
import platform

class Windows:
    
    def __init__(self):
        self.WORKDIR = None

    def getDisplayName(self):
        return "Microsoft Windows"

    def getMinecraftName(self):
        return "windows"

    def getLibrarySeparator(self):
        return ";"

    def getArchitecture(self):
        return platform.architecture()[0]

    def getWorkingDirectory(self):
        if self.WORKDIR != None:
            return self.WORKDIR
        appdata = os.getenv('APPDATA')
        if os.path.exists(appdata):
            if os.path.exists(appdata + "\.minecraft"):
                self.WORKDIR = appdata + "\.minecraft"
    
            return self.WORKDIR
        
    def setWorkingDirectory(self, Wdir):
        self.WORKDIR = Wdir

