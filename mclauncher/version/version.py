class Version(object):

    def __init__(self, id, type):
        self.id = id
        self.type = type
        
    def getID(self):
        return self.id
    
    def getType(self):
        return self.type