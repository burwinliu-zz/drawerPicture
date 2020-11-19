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
def uploadPic():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)    
    contents = s3.list_objects(Bucket='drawerbucket')['Contents']
    print(contents)

    try:
        enum = 0
        s3.upload_file("./tmp/captured.png", 'drawerbucket', f'captured_{enum}')
        return
    except NoCredentialsError:
        print("Bad Credentials")


def capturePic(path):
    if os.path.isfile(path + '/captured.jpg'):
        os.remove(path+'/captured.png')
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite(path + '/captured.png', image)
    del(camera)
    uploadPic()

if __name__ == "__main__":
    ser = serial.Serial(sys.argv[1], 9600)
    while 1: 
        s = ser.readline().decode('utf-8').strip()
        if s:
            print(s)
            if s == "1":
                # Take Picture on this action, and upload the item
                print("CORRECT")
                capturePic("./tmp")

