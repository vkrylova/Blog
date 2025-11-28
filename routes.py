from flask import jsonify, request

from app import app, db
from models import User


@app.route('/', methods=['GET'])
def home():
    return jsonify(message="Hello, Veronika!")


@app.route('/v1/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Invalid data'}), 400
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    if not email or not username or not password:
        return jsonify({'message': 'Missing fields'}), 400
    user = User(email=email, username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201
