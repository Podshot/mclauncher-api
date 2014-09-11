class YDLoginSessionID:

    def __init__(self, accessToken, clientToken):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getSession(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    
class YDPasswordLogin:
    
    def __init__(self, username, password, clientToken):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
    def getSession(self):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
    
class YDLogout:
    
    def __init__(self, session):
        raise TypeError("This API class must be overrided(or reference the 'implementation' package instead)")
        