from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call this API

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True)
