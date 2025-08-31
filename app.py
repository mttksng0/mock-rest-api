from flask import Flask, jsonify, request
app = Flask(__name__)

users = [{"id": 1, "first_name": "Baizhi"},
         {"id": 2, "first_name": "Chixia"}]


@app.route('/', methods=['GET'])
def get_home_page():
    if request.method == 'GET':
        return jsonify({"status": "ok"}), 200
    else:
        return 405


@app.route('/user/<int:id>', methods=['GET'])
def get_user_info(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True, port=443)
