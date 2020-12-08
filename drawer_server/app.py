from flask import Flask, send_file, jsonify, request
from flask_cors import CORS, cross_origin
import json
import boto3

from secrets import *
'''
AWS_ACCESS_KEY_ID
    The access key for your AWS account.
AWS_SECRET_ACCESS_KEY
    The secret key for your AWS account.

'''

app = Flask(__name__)
CORS(app)

DATA_LABELS = {'version': -1, 'labels': []}

def reloadPickle():
    try:
        with open('.\\tmp\\data.json', 'r') as fp:
            DATA_LABELS = json.load(fp)
    except IOError:
        print("No Saved Data")
    except json.decoder.JSONDecodeError:
        print("Data missaved, resetting")

def pollServer():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-east-2')    
    contents = s3.list_objects(Bucket='drawerbucket')['Contents'][0]
    if int(contents['Key'].split('_')[1]) != DATA_LABELS['version']:
        print("Updating Image")
        DATA_LABELS['version'] = contents['Key'].split('_')[1]
        with open('.\\tmp\\captured.png', 'wb') as fp:
            s3.download_fileobj('drawerbucket', contents['Key'], fp)
        with open('.\\tmp\\data.json', 'w') as fp:
            json.dump(DATA_LABELS, fp)
        
        # Triger rekognition and check for new entities
        rek=boto3.client('rekognition', aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-east-2')
        print(contents['Key'])
        response = rek.detect_labels(Image={'S3Object':{'Bucket':'drawerbucket','Name':contents['Key']}},
            MinConfidence =80)
        print(response)
        for i in response['Labels']:
            objName = i['Name']
            if objName not in DATA_LABELS['labels']:
                DATA_LABELS['labels'].append(objName)

# Todo: check if image data is latest. If not, reload it, and add any new labels
@app.route("/get_image")
def getImage():
    pollServer()
    return send_file('.\\tmp\\captured.png', mimetype='image/png')


@app.route("/get_labels")
def getLabels():

    with open('.\\tmp\\data.json', 'w') as fp:
        json.dump(DATA_LABELS, fp)
    return jsonify(DATA_LABELS)

@app.route("/add_labels")
def addLabels():
    newLabel = request.args.get('label')
    if newLabel is not None:
        DATA_LABELS['labels'].append(newLabel)
        with open('.\\tmp\\data.json', 'w') as fp:
            json.dump(DATA_LABELS, fp)
    return ""   

if __name__ == "__main__":
    reloadPickle()

    app.run()   