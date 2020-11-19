# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import serial
import sys
import cv2

def capturePic(path):

    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite(path + '/captured.jpg', image)
    del(camera)

if __name__ == "__main__":
    ser = serial.Serial(sys.argv[1], 9600)
    while 1: 
        s = ser.readline().decode('utf-8').strip()
        if s:
            print(s)
            if s == "1":
                # Take Picture on this action, and upload the item
                print("CORRECT")
                capturePic("/tmp")

