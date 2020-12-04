from flask import Flask, send_file, jsonify

from secrets import *
'''
AWS_ACCESS_KEY_ID
    The access key for your AWS account.
AWS_SECRET_ACCESS_KEY
    The secret key for your AWS account.

'''

app = Flask(__name__)

DATA_LABELS = {'version': 0, 'labels': []}

def reloadPickle():
    try:
        with open('.\\tmp\\data.json', 'r') as fp:
            DATA_LABELS = json.load(fp)
    except IOError:
        print("No Saved Data")

def pollServer():
    


@app.route("/get_image")
def getImage():
    return send_file('.\\tmp\\captured.png', mimetype='image/png')


@app.route("/get_labels")
def getLabels():

    with open('.\\tmp\\data.json', 'w') as fp:
        json.dump(DATA_LABELS, fp)
    return jsonify(DATA_LABELS)


if __name__ == "__main__":
    reloadPickle()

    app.run()   