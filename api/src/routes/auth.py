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
    return 'register'
