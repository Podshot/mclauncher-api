import os
import platform

WORKDIR = None

def getDisplayName():
    return "MAC OS"

def getMinecraftName():
    return "macos"

def getLibrarySeparator():
    return ":"

def getArchitecture():
    return platform.architecture()[0]

def getWorkingDirectory():
    if WORKDIR != None:
        return WORKDIR
    home = os.path.expanduser("~")
    if os.path.exists(home):
        if os.path.exists(home + "\Library/Application Support/.minecraft"):
            WORKDIR = home + "Library/Application Support/.minecraft"
    
    return WORKDIR