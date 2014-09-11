import json
import httplib
from mclauncher.implementation.utils import HTTPUtil
from mclauncher.api.login import YDLogin_API
from mclauncher.implementation.login import Session

headers = {
    'User-Agent': 'mclauncher',
    'Content-Type': "application/json"
    }
class YDLoginSessionID(YDLogin_API.YDLoginSessionID):
    
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
        jsonResponse = json.loads(http.getResponse().read())
        if jsonResponse["error"] == "" and jsonResponse["errorMessage"] == "":
            self.session = Session.Session(jsonResponse)
        else:
            raise Exception(jsonResponse["error"] + " - " + jsonResponse["errorMessage"])
        
    def getSession(self):
        return self.session
        
        

        
        
class YDPasswordLogin(YDLogin_API.YDPasswordLogin):
    
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
        jsonResponse = json.loads(http.getResponse().read())
        if "error" not in jsonResponse or "errorMessage" not in jsonResponse:
            self.session = Session.Session(jsonResponse)
        else:
            raise Exception(jsonResponse["error"] + " - " + jsonResponse["errorMessage"])
        
    def getSession(self):
        return self.session
    
class YDLogout(YDLogin_API.YDLogout):
    
    def __init__(self, session):
        logoutRequest = {}
        logoutRequest["accessToken"] = session.getAccessToken()
        logoutRequest["clientToken"] = session.getClientToken()
        
        logoutJSON = json.dumps(logoutRequest)
        http = HTTPUtil.HTTPSPost("authserver.mojang.com", "/invalidate", logoutJSON)
        jsonResponse = json.loads(http.getResponse().read())
        if jsonResponse["error"] != "" and jsonResponse["errorMessage"] != "":
            raise Exception(jsonResponse["error"] + " - " + jsonResponse["errorMessage"])
        
        
#YDLoginSessionID("aT", "cT")
#YDPasswordLogin("test", "test-password", "cT")