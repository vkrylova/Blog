from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import BadRequest, NotFound

from app import app, db
from models import User, Post


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


@app.route('/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        raise BadRequest('Invalid data')
    email = data.get('email')
    password = data.get('password')
    token, _ = User.authenticate(email, password)
    if not token:
        raise BadRequest('Invalid credentials')
    return jsonify({'access_token': token}), 200


@app.route('/v1/posts', methods=['POST'])
@jwt_required()
def add_posts():
    user_id = int(get_jwt_identity())
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    if not title or not body:
        raise BadRequest('Missing fields')
    post = Post(title=title, body=body, author_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify(message='Post added successfully')


@app.route('/v1/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify(posts=[post.to_dict() for post in posts]), 200


@app.route('/v1/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    if post := Post.query.get(post_id):
        return jsonify(posts=post.to_dict()), 200
    else:
        raise NotFound('Post not found')


@app.route('/v1/posts/<int:post_id>', methods=['PATCH'])
@jwt_required()
def update_post(post_id):
    user_id = int(get_jwt_identity())
    post = Post.query.get(post_id)
    if not post:
        raise NotFound('Post not found')
    if post.author_id != user_id:
        raise BadRequest('You are not authorized to update this post')
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)
    db.session.commit()
    return jsonify(message='Post updated successfully'), 200
