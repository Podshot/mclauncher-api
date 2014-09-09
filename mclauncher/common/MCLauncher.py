import urllib
import atexit
import subprocess
import Platform

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
        
        
        