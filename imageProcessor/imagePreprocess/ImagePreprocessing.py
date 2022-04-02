import sys
from MedianFilter import MedianFilter 
from OtsuThresholding import OtsuThresholding
from Dilation import Dilation
sys.path.append('G:\SourceCode\python\PoolCheater\imageProcessor') 
from ImageReaderAndWriter import ImageReaderAndWriter

class ImagePreprocessing:
    imageReaderAndWriter=ImageReaderAndWriter()
    billiardImage=imageReaderAndWriter.readImage()
    billiardTable=imageReaderAndWriter.getImageArray(billiardImage)
    
    
    medianFilter=MedianFilter(billiardTable)
    billiardTable=medianFilter.calculate()
    
    otsuThresholding=OtsuThresholding(billiardTable)
    billiardTable=otsuThresholding.calculate()
    
    dilation=Dilation(billiardTable)
    billiardTable=dilation.calculate(3)
    
    newImage=imageReaderAndWriter.getImageFromArray(billiardTable)
    imageReaderAndWriter.showImage(newImage)