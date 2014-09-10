from mclauncher.utils import HTTPUtil
import json

class AssetHandler(object):

    def __init__(self, assets):
        assetsJSON = json.loads(HTTPUtil.HTTPGet("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", assets)).getResponse())
        for entry in assetsJSON["objects"]:
            print entry
        HTTPUtil.DownloadFile("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", assets), "1.8.json")
        
        
        
AssetHandler("1.8")