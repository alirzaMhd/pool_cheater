from PIL import Image
import numpy as np

class ImageReaderAndWriter:
    def readImage(self):
        IMAGE_NAME="G:\SourceCode\python\PoolCheater\imageProcessor/billiard.jpg"
        billiardTable = Image.open(IMAGE_NAME).convert("L")
        return billiardTable
    
    def getImageArray(self,billiardTable):
        billiardTableArray=np.array(billiardTable)
        return billiardTableArray
    
    def getImageFromArray(self,billiardTableArray):
        billiardImage = Image.fromarray(billiardTableArray)
        return billiardImage
    
    def saveImage(self,billiardImage):
        billiardImage.convert("RGB")
        billiardImage.save("smoothed.png")
        
    def showImage(self,billiardImage):
        billiardImage.show()