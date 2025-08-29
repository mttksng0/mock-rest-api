from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home_page():
    if request.method == 'GET':
        return jsonify({"status": "ok"}), 200
    else:
        return 405


if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True, port=443)
