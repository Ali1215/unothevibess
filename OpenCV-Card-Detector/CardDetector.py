# Import necessary packages
import cv2
from cv2 import *
import numpy as np
import time
import os
import Cards
from card import card
from skimage.metrics import structural_similarity as ssim


### ---- MAIN LOOP ---- ###
def identify_card():
    
    #sets up camera and takes photo of what it captured and saves it into capture_card.jpg
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)   # 0 -> index of camera
    s, image = cam.read()
    image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("capture_card.jpg",image)

    # Pre-process camera image (gray, blur, and threshold it)
    pre_proc = Cards.preprocess_image(image)

    # Find and sort the contours of all cards in the image (query cards)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

    # If there are no contours, do nothing
    if len(cnts_sort) != 0:
        
        card = (Cards.preprocess_card(cnts_sort[0],image)) #flattens image
        cv2.imwrite("processed.jpg",card.warp)
        processedCard = card.warp
        maxScore = -2
        tempScore=-2
        maxFileName = ''
        
        for file in os.listdir("./OpenCV-Card-Detector/unoCardPictures"):
            #print(file)
            template = cv2.imread("./OpenCV-Card-Detector/unoCardPictures/"+file)
            #calculate correlation coefficient using scikit-image, structural similarity index
            tempScore = ssim(processedCard, template,win_size=11,multichannel=True)
            
            if tempScore>maxScore:
                maxScore = tempScore
                maxFileName = file
        print(maxFileName)    
        
    
        #parse the file name to get card info
        num = 0
        if (maxFileName[-7] == '-'):
            num = -1*int(maxFileName[-5])
        else:
            num = int(maxFileName[-5])
        return maxFileName[0].upper(), num
