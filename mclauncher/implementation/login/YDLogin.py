import json
import requests
import httplib
from mclauncher.implementation.utils import HTTPUtil

headers = {
    'User-Agent': 'mclauncher',
    'Content-Type': "application/json"
    }
class YDLoginSessionID(object):
    
    def __init__(self, accessToken, clientToken):
        sessionDict = {}
        sessionDict["clientToken"] = clientToken
        sessionDict["accessToken"] = accessToken
        sessionDict["selectedProfile"] = None
        # A Python None object is automatically converted to a null object in JSON
        sessionJSON = json.dumps(sessionDict)
        #response = requests.post("https://authserver.mojang.com/refresh", data=sessionJSON, allow_redirects=True)
        conn = httplib.HTTPSConnection("authserver.mojang.com")
        conn.request("POST", "/refresh", sessionJSON, headers)
        res = conn.getresponse()
        print "Status: " + str(res.status)
        print "Reason: " + str(res.reason)
        print "Response: " + res.read()
        
        http = HTTPUtil.HTTPSPost("authserver.mojang.com", "/refresh", sessionJSON)
        print http.getResponse().read()
        

        
        
class YDPasswordLogin(object):
    
    def __init__(self, username, password, clientToken):
        passwordLoginDict = {}
        agentDict = {}
        agentDict["name"] = "Minecraft"
        agentDict["version"] = "1"
        passwordLoginDict["agent"] = agentDict
        passwordLoginDict["username"] = username
        passwordLoginDict["password"] = password
        passwordLoginDict["clientToken"] = clientToken
        passwordLoginJSON = json.dumps(passwordLoginDict)
        
        http = HTTPUtil.HTTPSPost("authserver.mojang.com", "/authenticate", passwordLoginJSON)
        print http.getResponse().read()
        
        
#YDLoginSessionID("aT", "cT")
#YDPasswordLogin("test", "test-password", "cT")