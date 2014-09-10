import urllib2
import httplib
 
class HTTPGet(object):

    def __init__(self, url):
        return urllib2.urlopen(url).read()
    
    
class HTTPSPost(object):
    defaultHeader = {'User-Agent': 'mclauncher','Content-Type': "application/json"}
    
    def __init__(self, url, page, data, headers=None):
        if headers == None:
            headers = self.defaultHeader
        connection = httplib.HTTPSConnection(url)
        connection.request("POST", page, data, headers)
        self.response = connection.getresponse()
        
    def getResponse(self):
        return self.response
        
        