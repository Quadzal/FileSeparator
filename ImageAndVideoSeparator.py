import os
import shutil
class Separator:

    def __init__(self, path = os.getcwd(), outputPath = os.getcwd()):
        self.path = path
        self.outputPath = outputPath
        
        self.supportedImageTypes = ["jpg", "png", "raw", "gif", ".ico"]
        self.imagesPath = self.outputPath + "/images"
        
        self.videosPath = self.outputPath + "/videos"
        self.supportedVideoTypes = ["avi", "mp4", "vmw", "flv",
                                    "mov", "mpg", "mpeg"]
    
    def makeDirectory(self):
        try:
            os.mkdir(self.outputPath + "/images")
            os.mkdir(self.outputPath + "/videos")
        except FileExistsError:
            pass
    
    def ImageSeparator(self):
        os.chdir(self.path)
        for topDir, subDir, files in os.walk(self.path):
            for file in files:
                filePath = topDir + "\\" + file
                if(file[-3:] in self.supportedImageTypes):
                    
                    shutil.move(filePath, self.imagesPath)
    
    def VideoSeparator(self):
        os.chdir(self.path)
        for topDir, subDir, files in os.walk(self.path):
            for file in files:
                filePath = topDir + "\\" + file
                if(file[-3:] in self.supportedVideoTypes):
                    shutil.move(filePath, self.videosPath)

    def start(self):
        self.makeDirectory()
        self.ImageSeparator()
        self.VideoSeparator()
