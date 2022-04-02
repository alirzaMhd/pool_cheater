
import numpy as np

class OtsuThresholding:
    def __init__(self, imageArray):
        self.imageArray=imageArray
    def calculate(self):
        pixelCounts = [np.sum(self.imageArray == i) for i in range(256)]

        mostCommonPixel = (0,0)
        for threshold in range(256):


            w_0 = sum(pixelCounts[:threshold])
            w_1 = sum(pixelCounts[threshold:])

            mu_0 = sum([i * pixelCounts[i] for i in range(0,threshold)]) / w_0 if w_0 > 0 else 0       
            mu_1 = sum([i * pixelCounts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0


            newPixel = np.clongdouble(w_0 * w_1 * (mu_0 - mu_1) ** 2)
            if newPixel > mostCommonPixel[1]:
                mostCommonPixel = (threshold, newPixel)
        print(mostCommonPixel)
        return ((self.imageArray > mostCommonPixel[0]) * 255).astype('uint8')

