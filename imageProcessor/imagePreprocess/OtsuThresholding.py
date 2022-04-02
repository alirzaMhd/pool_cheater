
import numpy as np

class OtsuThresholding:
    def __init__(self, imageArray):
        self.imageArray=imageArray
        
    def getImageHistogram(self,imageArray):
        hist=np.histogram( imageArray, 256 )[0]
        return hist
    
    def calculate(self):
        hist=self.getImageHistogram(self.imageArray)
        
        ROW, COLS = np.shape( self.imageArray )
        TOTAL=ROW*COLS
        HISTOGRAM_LENGTH = len(hist)
        sum_total = 0
        for x in range( 0, HISTOGRAM_LENGTH ):
            sum_total += x * hist[x]
	
        weight_background= 0.0
        sum_background= 0.0
        inter_class_variances= []

        for threshold in range( 0, HISTOGRAM_LENGTH ):
            weight_background+= hist[threshold]
            if (weight_background == 0) :
                continue

            weight_foreground = TOTAL - weight_background
            if (weight_foreground == 0 ):
                break

            sum_background+= threshold * hist[threshold]
            mean_background= sum_background / weight_background
            mean_foreground= (sum_total - sum_background) / weight_foreground

            inter_class_variances.append( weight_background * weight_foreground * (mean_background - mean_foreground)**2 )

        return ((self.imageArray > np.argmax(inter_class_variances)) * 255).astype('uint8')