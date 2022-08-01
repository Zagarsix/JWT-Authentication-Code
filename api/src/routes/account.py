from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Profile

account = Blueprint('account', __name__)

@account.route('/profile', methods=['GET'])
@jwt_required()
def login():
    return 'Profile'
