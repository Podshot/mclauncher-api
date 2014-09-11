from mclauncher.api.login import Session_API

class Session(Session_API.Session):

    def __init__(self, sessionJSON):
        self.accessToken = sessionJSON["accessToken"]
        self.clientToken = sessionJSON["clientToken"]
        self.profile = self.Profile(sessionJSON["selectedProfile"])
        
        
    class Profile(Session_API.Session.Profile):
        
        def __init__(self, profileJSON):
            return
        
        