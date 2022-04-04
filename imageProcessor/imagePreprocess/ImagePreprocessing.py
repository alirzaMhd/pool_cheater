import sys
from MedianFilter import MedianFilter 
from Dilation import Dilation
from IntegralThreshold import IntegralThreshold

class ImagePreprocessing:
    def __init__(self,billiardTable) :
        self.billiardTable=billiardTable
    
    def calculator(self):
        medianFilter=MedianFilter(self.billiardTable)
        billiardTable=medianFilter.calculate()
    
        integralThreshold=IntegralThreshold(billiardTable)
        billiardTable=integralThreshold.calculate()
    
        dilation=Dilation(billiardTable)
        billiardTable=dilation.calculate(3)
    
    
    
    