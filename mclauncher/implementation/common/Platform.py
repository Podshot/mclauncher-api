from sys import platform as _platform
import Windows
import Macintosh
from mclauncher.api.common import Platform_API

class Platform(Platform_API.Platform):
    
    def __init__(self):
        if _platform == "win32":
            self.os = Windows.Windows()
        if _platform == "darwin":
            self.os = Macintosh

    def getWorkingDirectory(self):
        return self.os.getWorkingDirectory()
    
    def setWorkingDirectory(self, Wdir):
        self.os.setWorkingDirectory(Wdir)
        