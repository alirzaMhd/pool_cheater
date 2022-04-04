import sys
sys.path.append('G:\SourceCode\python\PoolCheater\imageProcessor\ImagePreprocess') 
from ImagePreprocessing import ImagePreprocessing
from ImageReaderAndWriter import ImageReaderAndWriter

class ImageProcessing:
    
    def HandleImageReading():
        imageReaderAndWriter=ImageReaderAndWriter()
        billiardImage=imageReaderAndWriter.readImage()
        billiardImage=imageReaderAndWriter.makeImageGrayscale(billiardImage)
        billiardTable=imageReaderAndWriter.getImageArray(billiardImage)
        return billiardTable
    
    billiardTable=HandleImageReading()
    
    imagePreprocessing=ImagePreprocessing(billiardTable)
    billiardTable=imagePreprocessing.calculator()