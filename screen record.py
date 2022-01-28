import pyautogui
import cv2
import numpy as np

resolution = (1920,1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "Recording.avi"

fps = 60.0

out = cv2.VideoWriter(filename, codec, fps,resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live",480,270)