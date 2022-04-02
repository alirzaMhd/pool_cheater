import numpy as np

class Dilation:
    def __init__(self, imageArray):
        self.imageArray=imageArray
        
    def calculate(self,dilation_level):
        dilation_level=3 if dilation_level<3 else dilation_level
        KERNEL=np.full(shape=(dilation_level,dilation_level),fill_value=255)
        widthPad = dilation_level - 2
        originalShape = self.imageArray.shape
        imagePad = np.pad(array=self.imageArray, pad_width=widthPad, mode='constant')
        imageWithPad = imagePad.shape
        h_reduce, w_reduce = (imageWithPad[0] - originalShape[0]), (imageWithPad[1] - originalShape[1])
        flat_submatrices = np.array([
            imagePad[i:(i + dilation_level), j:(j + dilation_level)]
            for i in range(imageWithPad[0] - h_reduce) for j in range(imageWithPad[1] - w_reduce)
        ])
        dilatedImage = np.array([255 if (i == KERNEL).any() else 0 for i in flat_submatrices])
        dilatedImage = dilatedImage.reshape(originalShape)
        return dilatedImage