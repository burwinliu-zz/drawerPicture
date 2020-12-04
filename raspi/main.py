# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import serial
import sys
import os
import cv2
import boto3
from botocore.exceptions import NoCredentialsError

from secrets import *
'''
AWS_ACCESS_KEY_ID
    The access key for your AWS account.
AWS_SECRET_ACCESS_KEY
    The secret key for your AWS account.

'''

ENUM = 0


def uploadPic():
    # s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
    #         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)    
    # contents = s3.list_objects(Bucket='drawerbucket')['Contents']
    # print(contents)

    try:
        # s3.upload_file("./tmp/captured.png", 'drawerbucket', f'captured_{ENUM}')
        ENUM += 1
        try:
            with open("./tmp/enum", "w+") as fp 
                # absolute file positioning 
                fp.seek(0)  
                
                # to erase all data  
                fp.truncate()  
                fp.write(ENUM)
        except IOError:

        
        return
    except NoCredentialsError:
        print("Bad Credentials")


def capturePic():
    if os.path.isfile('./tmp/captured.jpg'):
        os.remove('./tmp/captured.png')
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('./tmp/captured.png', image)
    del(camera)
    uploadPic()

if __name__ == "__main__":
    try:
        with open('./tmp_enum', 'r') as fp:
            ENUM = int(fp.readline())
    ser = serial.Serial(sys.argv[1], 9600)
    while 1: 
        s = ser.readline().decode('utf-8').strip()
        if s:
            if s == "1":
                # Take Picture on this action, and upload the item
                capturePic()

