from sys import platform as _platform
import os
import Windows
import Macintosh

def getCurrentPlatform():
    if _platform == "win32":
        return Windows.getDisplayName()
    if _platform == "darwin":
        return Macintosh.getDisplayName()
    return None

def getWorkingDirectory():
    return os.getcwd()