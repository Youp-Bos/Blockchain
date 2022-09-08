from flask import jsonify
from flask import Flask

app = Flask(__name__)

studenten = \
    [
        {'id': '1', 'name': 'Youp Bos', 'age': '19', 'gender': 'Male'},
        {'id': '2', 'name': 'Nour salama', 'age': '20', 'gender': 'Male'}
    ]

@app.route('/all/api', methods=['GET'])
def allApi():
    return jsonify(studenten)




app.run()
