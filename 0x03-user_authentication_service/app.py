#!/usr/bin/env python3
"""A basic Flask app set up"""


from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email, "message": "user created"})

    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
