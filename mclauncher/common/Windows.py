import os

WORKDIR = None

def getDisplayName():
    return "Mircosoft Windows"

def getMinecraftName():
    return "windows"

def getLibrarySeparator():
    return ";"

def getWorkingDirectory():
    if WORKDIR != None:
        return WORKDIR
    appdata = os.getenv('APPDATA')
    if (os.path.exists(appdata)):
        if os.path.exists(appdata + "/.minecraft"):
            WORKDIR = appdata + "/.minecraft"
    
    return WORKDIR
