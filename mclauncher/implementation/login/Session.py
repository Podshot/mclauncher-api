from mclauncher.api.login import Session_API

class Session(Session_API.Session):
    
    availableProfiles = []

    def __init__(self, sessionJSON):
        self.accessToken = sessionJSON["accessToken"]
        self.clientToken = sessionJSON["clientToken"]
        self.profile = SessionProfile(sessionJSON["selectedProfile"])
        for a_profile in sessionJSON["availableProfiles"]:
            self.availableProfiles.append(SessionProfile(a_profile))
            
    def getAccessToken(self):
        return self.accessToken
    
    def getClientToken(self):
        return self.clientToken
    
    def getSelectedProfile(self):
        return self.profile
    
    def getAvailableProfiles(self):
        return self.availableProfiles
        
class SessionProfile(Session_API.SessionProfile):
    
    def __init__(self, profileJSON):
        self.name = profileJSON["name"]
        self.id = profileJSON["id"]
        
    def getName(self):
        return self.name
    
    def getID(self):
        return self.getID()
        
        