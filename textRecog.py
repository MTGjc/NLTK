import socket
from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np

import os
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#setup folder to store images
image_frames = 'image_frames'
# testimage = pytesseract.image_to_string(Image.open('nltk0.png'))
# print(testimage)

def files():

    try:
        os.remove(image_frames)
    except OSError:
        pass

    if not os.path.exists(image_frames):
        os.makedirs(image_frames)
    
    # specify source video path
    src_vid = cv2.VideoCapture('Sequence 01.mp4')
    return(src_vid)

def process(src_vid):
    
    # name file
    index =0
    while src_vid.isOpened():
        ret, frame = src_vid.read()
        if not ret:
            break

        name = './image_frames/frame'+ str(index) + '.png'

        #save every 150 frame
        if index % 200 ==0:
            print ('Extract frame...'+ name)
            cv2.imwrite(name, frame)
        index = index +1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    src_vid.realise()
    cv2.destroyAllWindows()

# #image to text on each png

def get_text():
    for i in os.listdir(image_frames):
        my_example = Image.open(image_frames + "/" + i)
        text = pytesseract.image_to_string(my_example, lang='eng+chi_sim')
        print (text)

# #main drive
if __name__ == '__main__':
    vid = files()
    process(vid)
    get_text()