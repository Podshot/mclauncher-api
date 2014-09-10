import urllib
import atexit
import subprocess
import Platform
from mclauncher.version.assets import AssetHandler

class MCLauncher(object):

    def __init__(self, version):
        self.version = version
        self.getVersionJSON()
    
    def getJar(self):
        urllib.urlretrieve(self.version.getJarURL(), self.version.getJarName())
        
    def downloadResources(self):
        return
    
    def getVersionJSON(self):
        self.versionJSON = self.version.getVersionJSON()
    
    def install(self):
        assets = self.version.getAssets()
        AssetHandler.AssetHandler(assets)
        
    def startGame(self, arguments):
        proc = subprocess.Popen(arguments,
                                 executable=self.javaEXE,
                                 cwd=Platform.getWorkingDirectory(),
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 universal_newlines=True,)
        atexit.register(proc.terminate())
        return proc
        
        
        