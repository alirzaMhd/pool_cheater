import sys
from MedianFilter import MedianFilter 
sys.path.append('G:\SourceCode\python\PoolCheater\imageProcessor') 
from ImageReaderAndWriter import ImageReaderAndWriter

class ImagePreprocessing:
    imageReaderAndWriter=ImageReaderAndWriter()
    billiardTable=imageReaderAndWriter.getImageArray()
    
    
    medianFilter=MedianFilter(billiardTable)
    billiardTableProcessed=medianFilter.calculate()
    
    
    
    
    newImage=imageReaderAndWriter.getImageFromArray(billiardTableProcessed)
    imageReaderAndWriter.showImage(newImage)