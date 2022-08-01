from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Profile

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    return 'login'

@auth.route('/register', methods=['POST'])
def register():
    # user
    email = request.json.get('email')
    password = request.json.get('password')

    # profile
    name = request.json.get('name', '')
    biography = request.json.get('biography', '')
    
    # check if user already exist
    userFound = User.query.filter_by(email = email).first()

    if userFound: return jsonify({'status': 'failed', 'message': 'User already exist', 'data': None}), 400

    if not email: return jsonify({'status': 'failed', 'message': 'Email is required', 'data': None}), 400

    if not password: return jsonify({'status': 'failed', 'message': 'Password is required', 'data': None}), 400

    # if user doesn't exist, create user and create profile
    user = User()
    user.email = email
    user.password = generate_password_hash(password)

    profile = Profile()
    profile.name = name
    profile.biography = biography

    user.profile = profile
    user.save()

    # if register succeded
    if user: return jsonify({'status': 'success', 'message': 'Registered successfully, please login', 'data': None}), 200
    else: return jsonify({'status': 'failed', 'message': 'Error in register, please try again', 'data': None}), 200

