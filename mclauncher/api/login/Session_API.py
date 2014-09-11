class Session:

    def __init__(self, sessionJSON):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getAccessToken(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getClientToken(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getSelectedProfile(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getAvailableProfiles(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    class Profile:
        
        def __init__(self, profileJSON):
            raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
        
        def getName(self):
            raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
        
        def getID(self):
            raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")

        