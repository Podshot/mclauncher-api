class OS:
    
    def __init__(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")

    def getDisplayName(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")

    def getMinecraftName(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")

    def getLibrarySeparator(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")

    def getArchitecture(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")

    def getWorkingDirectory(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
        
    def setWorkingDirectory(self, Wdir):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")