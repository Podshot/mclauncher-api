class Platform:

    def __init__(self, params):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getWorkingDirectory(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
        
        