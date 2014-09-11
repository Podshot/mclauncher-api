import os
import platform

WORKDIR = None

def getDisplayName():
    return "Linux/Unix"

def getMinecraftName():
    return "linux"

def getLibrarySeparator():
    return ":"

def getArchitecture():
    return platform.architecture()[0]

def getWorkingDirectory():
    if WORKDIR != None:
        return WORKDIR
    home = os.path.expanduser("~")
    if os.path.exists(home):
        if os.path.exists(home + "/.minecraft"):
            WORKDIR = home + "/.minecraft"
    
    return WORKDIR