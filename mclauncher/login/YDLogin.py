import json

class YDLoginSessionID(object):
    
    def __init__(self, accessToken, clientToken):
        sessionDict = {}
        sessionDict["clientToken"] = clientToken
        sessionDict["accessToken"] = accessToken
        sessionDict["selectedProfile"] = None
        print sessionDict
        
        
YDLoginSessionID("aT", "cT")