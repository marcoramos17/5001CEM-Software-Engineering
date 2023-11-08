from PIL import Image
import numpy as np
import os
import cv2

rootDir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# Only run if the data has been cached previously
animals=np.load(rootDir + "\\data\\animalCache.npy")
labels=np.load(rootDir + "\\data\\labelsCache.npy")

with open(rootDir + "\\data\\animals\\names.txt", 'r') as names:
    animalNames = []
    for name in names:
        animalNames.append(name.rstrip('\n'))

# The following code is only required on first run, data is saved to numpy files
# for easy access in later file runs
'''
animals=[]
labels=[]

counter = 0
for animal in animalNames:
    fileList = os.listdir(rootDir + "\\data\\animals\\" + animal)
    for image in fileList:
        cv2Image = cv2.imread(rootDir + "\\data\\animals\\" + animal + "\\" + image)
        PILImage = Image.fromarray(cv2Image, 'RGB')
        resizedImage = PILImage.resize((50, 50))
        animals.append(np.array(resizedImage))
        labels.append(counter)
    counter += 1

animals=np.array(animals)
labels=np.array(labels)

np.save(rootDir + "\\data\\animalCache",animals)
np.save(rootDir + "\\data\\labelsCache",labels)
'''

