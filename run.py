import cv2
from gaze_tracking import GazeTracking
from tkinter import *
from time import time
import pyautogui

left = 0.0
right = 0.0
top = 0.0
bottom = 0.0
width = 1920
height = 1040
mode = 0

gaze = GazeTracking()
webcam = cv2.VideoCapture(1)

recordedRatios = []
stopwatch = time()
currentCount = 0
xRatios = []
yRatios = []
recording = False

def horizontalLocation(ratio):
    if ratio is None:
        return None
    global left, right, width
    return width - min(width, max(0, (ratio - right) / (left - right) * width))
    
def verticalLocation(ratio):
    if ratio is None:
        return None
    global top, bottom, height
    return min(height, max(0, (ratio - top) / (bottom - top) * height))

def checkFrame():
    global left, right, top, bottom, currentCount, recordedRatios, stopwatch, xRatios, yRatios, recording, mode
    _, frame = webcam.read()

    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    cv2.imshow("Camera", frame)
    
    if currentCount < 4 and recording:
        match currentCount:
            case 0 | 1:
                recordedRatios.append(gaze.horizontal_ratio())
            case 2 | 3:
                recordedRatios.append(gaze.vertical_ratio())
    elif not recording and len(recordedRatios) != 0:
        match currentCount:
            case 0:
                recordedRatios = list(filter(lambda i: i is not None, recordedRatios))
                left = sum(recordedRatios) / len(recordedRatios)
                currentCount += 1
                recordedRatios = []
                stopwatch = time()
                print("Left", left)
            case 1:
                recordedRatios = list(filter(lambda i: i is not None, recordedRatios))
                right = sum(recordedRatios) / len(recordedRatios)
                currentCount += 1
                recordedRatios = []
                stopwatch = time()
                print("Right", right)
            case 2:
                recordedRatios = list(filter(lambda i: i is not None, recordedRatios))
                top = sum(recordedRatios) / len(recordedRatios)
                currentCount += 1
                recordedRatios = []
                stopwatch = time()
                print("Top", top)
            case 3:
                recordedRatios = list(filter(lambda i: i is not None, recordedRatios))
                bottom = sum(recordedRatios) / len(recordedRatios)
                currentCount += 1
                recordedRatios = []
                print("Bottom", bottom)
    elif currentCount > 3:
        x = gaze.horizontal_ratio()
        y = gaze.vertical_ratio()
        if x is not None and y is not None:
            xRatios.append(x)
            yRatios.append(y)
        if len(xRatios) >= 10:
            xloc = horizontalLocation(sum(xRatios) / len(xRatios))
            yloc = verticalLocation(sum(yRatios) / len(yRatios))
            print(xloc, yloc)
            xRatios.pop(0)
            yRatios.pop(0)
            if (mode == 1):
                pyautogui.moveTo(xloc, yloc, 0.001)
            if (mode == 2):
                pyautogui.moveRel((-10 if xloc < width / 3 else 0) + (10 if xloc > width * 2 / 3 else 0), (-10 if yloc < height / 3 else 0) + (10 if yloc > height * 2 / 3 else 0), duration=.001)
    if cv2.waitKey(1) == 13:
        recording = not recording
    if cv2.waitKey(1) == 27:
        return
    checkFrame()

mode = int(input("Enter 1 for pure eye tracking, 2 for eye based mouse drift control: "))
checkFrame()

print("Left", left)
print("Right", right)
print("Top", top)
print("Bottom", bottom)
   
webcam.release()
cv2.destroyAllWindows()
