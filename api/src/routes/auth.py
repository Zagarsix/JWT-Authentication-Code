import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Profile

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    # user
    email = request.json.get('email')
    password = request.json.get('password')

    if not email: return jsonify({'status': 'failed', 'message': 'Email is required', 'data': None}), 400
    if not password: return jsonify({'status': 'failed', 'message': 'Password is required', 'data': None}), 400
    

    userExists = User.query.filter_by(email = email).first()
    # check if user does not exist
    if not userExists: return jsonify({'status': 'failed', 'message': 'Email/Password are incorrects', 'data': None}), 401
    # validate password, if the password of the user is different from the password being passed
    if not check_password_hash(userExists.password, password): 
        return jsonify({'status': 'failed', 'message': 'Email/Password are incorrects', 'data': None}), 401

    # expire date of access token
    expires = datetime.timedelta(days=1)

    # create access token    
    acces_token = create_access_token(identity = userExists.id, expires_delta= expires)

    data = {
        'access_token': acces_token,
        'user': userExists.serialize()
    }

    return jsonify({ "status": "success", "message": "Login successfully", "data": data }), 200


@auth.route('/register', methods=['POST'])
def register():
    # user
    email = request.json.get('email')
    password = request.json.get('password')

    # profile
    name = request.json.get('name', '')
    biography = request.json.get('biography', '')
    
    if not email: return jsonify({'status': 'failed', 'message': 'Email is required', 'data': None}), 400
    if not password: return jsonify({'status': 'failed', 'message': 'Password is required', 'data': None}), 400

    # check if user already exist
    userFound = User.query.filter_by(email = email).first()
    if userFound: return jsonify({'status': 'failed', 'message': 'User already exists', 'data': None}), 400


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

