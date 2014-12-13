from mclauncher.implementation.utils import HTTPUtil
from mclauncher.implementation.common import Platform
import json
import os
import sys

class AssetHandler:

    def __init__(self, assets):
        self.assetVer = assets
        print Platform.Platform.Instance().getWorkingDirectory() # @UndefinedVariable
        assetsJSON = json.loads(HTTPUtil.HTTPGet("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", assets)).getResponse())
        self.setupAssetsFolder()
        for entry in assetsJSON["objects"]:
            asset_hash = assetsJSON["objects"][entry]["hash"]
            asset_prefix = asset_hash[:2]
            asset_url = " http://resources.download.minecraft.net/<HASH_PART_1>/<HASH_COMPLETE>".replace("<HASH_PART_1>", asset_hash[:2])
            asset_url = asset_url.replace("<HASH_COMPLETE>", asset_hash)
            self.downloadAsset(asset_prefix, asset_hash, asset_url)
        #HTTPUtil.DownloadFile("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", assets), "1.8.json")
        
    def setupAssetsFolder(self):
        self.gameDir = Platform.Platform.Instance().getWorkingDirectory() # @UndefinedVariable
        try:
            os.mkdir(self.gameDir + "/assets")
        except OSError:
            print "Error creating assets"
            pass
        try:
            os.mkdir(self.gameDir + "/assets/indexes")
        except OSError:
            print "Error creating indexes"
            pass
        try:
            os.mkdir(self.gameDir + "/assets/objects")
        except OSError:
            print "Error creating objects"
            pass
        HTTPUtil.DownloadFile("https://s3.amazonaws.com/Minecraft.Download/indexes/<INDEX_NAME>.json".replace("<INDEX_NAME>", self.assetVer), self.gameDir + "\\assets\\indexes\\<VER>.json".replace("<VER>", self.assetVer))
        print "Setup Asset Folder"
        
    def downloadAsset(self, asset_prefix, asset_hash, asset_url):
        path = str(self.gameDir+os.path.sep+"assets"+os.path.sep+"objects"+os.path.sep+asset_prefix+os.path.sep+asset_hash)
        if os.path.exists(path):
            return
        asset_url = asset_url.replace(" ", "")
        HTTPUtil.downloadFile(asset_url, path)
        
        
#AssetHandler("1.8")