from flask import Flask, send_file, jsonify
from flask_cors import CORS, cross_origin
import json

from secrets import *
'''
AWS_ACCESS_KEY_ID
    The access key for your AWS account.
AWS_SECRET_ACCESS_KEY
    The secret key for your AWS account.

'''

app = Flask(__name__)
CORS(app)

DATA_LABELS = {'version': 0, 'labels': ['testlabel']}

def reloadPickle():
    try:
        with open('.\\tmp\\data.json', 'r') as fp:
            DATA_LABELS = json.load(fp)
    except IOError:
        print("No Saved Data")
    except json.decoder.JSONDecodeError:
        print("Data missaved, resetting")

def pollServer():
    pass

# Todo: check if image data is latest. If not, reload it, and add any new labels
@app.route("/get_image")
@cross_origin(origin='http://localhost:3000')
def getImage():
    return send_file('.\\tmp\\captured.png', mimetype='image/png')


@app.route("/get_labels")
def getLabels():

    with open('.\\tmp\\data.json', 'w') as fp:
        json.dump(DATA_LABELS, fp)
    return jsonify(DATA_LABELS)

@app.route("/add_labels")
def addLabels():
    pass

if __name__ == "__main__":
    reloadPickle()

    app.run()   