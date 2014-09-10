import urllib2
import urllib
import httplib
import os
 
class HTTPGet(object):

    def __init__(self, url):
        self.response = urllib2.urlopen(url).read()
    
    def getResponse(self):
        return self.response
    
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
    
class DownloadFile(object):
    
    def __init__(self, url, file):
        urllib.urlretrieve(url, file)
        print os.path.getsize("C:\\Users\\Jonathan\\Python\\mclauncher-api\\mclauncher-api\\mclauncher\\version\\assets\\1.8.json")
    
        
        