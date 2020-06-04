# -*- coding: utf-8 -*-
import sys
import cv2
import os

HOME = os.path.expanduser('~').split("\\")[-1]
PATH = "C:\\Users\\"+HOME+"\\AppData\\Roaming\\Python\\Python38\\site-packages"
print(PATH)
sys.path.append(PATH)

def video2frame(invideofilename, save_path):
    vidcap = cv2.VideoCapture(invideofilename)
    count = 0
    while True:
      success,image = vidcap.read()
      if not success:
          break
      print ('Read a new frame: ', success)
      fname = "{}.jpg".format("{0:05d}".format(count))
      cv2.imwrite(save_path + fname, image) # save frame as JPEG file
      count += 1
    print("{} images are extracted in {}.". format(count, save_path))

VIDEO_PATH = ""
STORED_PATH = ""
video2frame(VIDEO_PATH, STORED_PATH)
