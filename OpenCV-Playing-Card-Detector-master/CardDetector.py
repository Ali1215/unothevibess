# Import necessary packages
import cv2
from cv2 import *
import numpy as np
import time
import os
import Cards
import VideoStream
from card import card

from skimage.metrics import structural_similarity as ssim

### ---- INITIALIZATION ---- ###
# Define constants and initialize variables

## Camera settings
# Initialize camera object and video feed from the camera. The video stream is set up
# as a seperate thread that constantly grabs frames from the camera feed. 
# See VideoStream.py for VideoStream class definition
## IF USING USB CAMERA INSTEAD OF PICAMERA,
## CHANGE THE THIRD ARGUMENT FROM 1 TO 2 IN THE FOLLOWING LINE:
#videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,1,0).start()
#time.sleep(1) # Give the camera time to warm up

# Load the train rank and suit images
#path = os.path.dirname(os.path.abspath(__file__))
#train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
#train_suits = Cards.load_suits( path + '/Card_Imgs/')



### ---- MAIN LOOP ---- ###
# The main loop repeatedly grabs frames from the video stream
# and processes them to find and identify playing cards.
def identify_card():

    cam_quit = 0 # Loop control variable
    #cam = cv2.VideoCapture('http://192.168.1.68:4747/video')
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)   # 0 -> index of camera
    s, image = cam.read()
    image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("capture_card.jpg",image)

    #path1='./OpenCV-Playing-Card-Detector-master/WIN_20220116_02_43_47_Pro.jpg'

    #image = cv2.imread(path1)

    # Begin capturing frames


    # Grab frame from video stream



    print('hi')
    # Pre-process camera image (gray, blur, and threshold it)
    pre_proc = Cards.preprocess_image(image)

    # Find and sort the contours of all cards in the image (query cards)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)
    print('hi')
    # If there are no contours, do nothing
    if len(cnts_sort) != 0:
        print('hi')
        # Initialize a new "cards" list to assign the card objects.
        # k indexes the newly made array of cards.
        
        card = (Cards.preprocess_card(cnts_sort[0],image))
        cv2.imwrite("processed.jpg",card.warp)
        processedCard = card.warp
        maxScore = -2
        tempScore=-2
        maxFileName = ''
        #print(os.listdir("./OpenCV-Playing-Card-Detector-master/unoCardPictures/"))
        for file in os.listdir("./OpenCV-Playing-Card-Detector-master/unoCardPictures"):
            #print(file)
            template = cv2.imread("./OpenCV-Playing-Card-Detector-master/unoCardPictures/"+file)
            tempScore = ssim(processedCard, template,win_size=11,multichannel=True)
            #print(file + str(tempScore))
            #print(maxScore)
            #print(maxFileName)
            if tempScore>maxScore:
                maxScore = tempScore
                maxFileName = file
        print(maxFileName)    
        
    

        num = 0
        if (maxFileName[-7] == '-'):
            num = -1*int(maxFileName[-5])
        else:
            num = int(maxFileName[-5])
        return maxFileName[0].upper(), num


        
        
        
        
        

        

    # Close all windows and close the PiCamera video stream.
    cv2.destroyAllWindows()


