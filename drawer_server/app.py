from flask import Flask, send_file, jsonify
app = Flask(__name__)

DATA_LABELS = {'version': 0, 'labels': []}

def reloadPickle():
    pass


@app.route("/get_image")
def getImage():
    return send_file('.\\tmp\\captured.png', mimetype='image/png')


@app.route("/get_labels")
def getLabels():
    return jsonify(DATA_LABELS)


if __name__ == "__main__":
    reloadPickle()

    app.run()