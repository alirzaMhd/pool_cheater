import cv2
import numpy as np
class IntegralThreshold:
    
    def __init__(self, imageArray):
        self.imageArray=imageArray
        
    def calculate(self,T = 0.15):
        integralImage = cv2.integral(self.imageArray)
        thresholdImage=np.zeros(self.imageArray.shape)
        ROWS = self.imageArray.shape[0]
        COLS = self.imageArray.shape[1]
        S = int(max(ROWS, COLS) / 8)

        s2 = int(S / 4)

        for i in range(ROWS):
            y1 = i - s2
            y2 = i + s2

            if (y1 < 0) :
                y1 = 0
            if (y2 >= ROWS):
                y2 = ROWS - 1

            for j in range(COLS):
                x1 = j - s2 
                x2 = j + s2

                if (x1 < 0) :
                    x1 = 0
                if (x2 >= COLS):
                    x2 = COLS - 1
                count = (x2 - x1)*(y2 - y1)

                sum=integralImage[y2][x2]-integralImage[y2][x1]-integralImage[y1][x2]+integralImage[y1][x1]

                if ((int)(self.imageArray[i][j] * count) < (int)(sum*(1.0 - T))):
                    thresholdImage[i][j] = 255
        return thresholdImage