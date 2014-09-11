from sys import platform as _platform
import Windows
import Macintosh
from mclauncher.api.common import Platform_API

class Strict_Platform(Platform_API.Platform):
    
    def __init__(self):
        if _platform == "win32":
            self.os = Windows
        if _platform == "darwin":
            self.os = Macintosh

    def getWorkingDirectory(self):
        return self.os.getWorkingDirectory()
    
class Flexible_Platform(Platform_API.Platform):
    
    __shared_state = {}
    
    def __init__(self):
        if _platform == "win32":
            self.os = Windows
        if _platform == "darwin":
            self.os = Macintosh
        self.workingDirectory = self.os.getWorkingDirectory()
    
    def setWorkingDirecotry(self, wDir):
        self.workingDirectory = wDir
        
    def getWorkingDirectory(self):
        return self.workingDirectory
        