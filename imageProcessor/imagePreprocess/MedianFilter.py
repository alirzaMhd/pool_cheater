import numpy as np


class MedianFilter:
    def __init__(self, imageArray):
        self.imageArray=imageArray
    def calculate(self):
        KERNEL=3
        INDEXER = KERNEL // 2
        temp = []
        finalImage = []
        finalImage = np.zeros((len(self.imageArray),len(self.imageArray[0])))
        for i in range(len(self.imageArray)):

            for j in range(len(self.imageArray[0])):

                for z in range(KERNEL):
                    if i + z - INDEXER < 0 or i + z - INDEXER > len(self.imageArray) - 1:
                        for c in range(KERNEL):
                            temp.append(0)
                    else:
                        if j + z - INDEXER < 0 or j + INDEXER > len(self.imageArray[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(KERNEL):
                                temp.append(self.imageArray[i + z - INDEXER][j + k - INDEXER])

                temp.sort()
                finalImage[i][j] = temp[len(temp) // 2]
                temp = []
        return finalImage