from mclauncher.implementation.utils import HTTPUtil
import json

class AssetHandler(object):

    def __init__(self, assets):
        assetsJSON = json.loads(HTTPUtil.HTTPGet("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", assets)).getResponse())
        for entry in assetsJSON["objects"]:
            asset_hash = assetsJSON["objects"][entry]["hash"]
            print asset_hash[:2]
            asset_url = " http://resources.download.minecraft.net/<HASH_PART_1>/<HASH_COMPLETE>".replace("<HASH_PART_1>", asset_hash[:2])
            asset_url = asset_url.replace("<HASH_COMPLETE>", asset_hash)
        #HTTPUtil.DownloadFile("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", assets), "1.8.json")
        
        
        
AssetHandler("1.8")