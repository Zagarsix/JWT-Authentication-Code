from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from routes.auth import auth
from routes.account import account

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'secret-key'

db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade
jwt = JWTManager(app)
CORS(app)

### Code between this lines ###

app.register_blueprint(auth, url_prefix='/api')
app.register_blueprint(account, url_prefix='/api')

@app.route('/')
def root():
    return jsonify({"message": "Welcome to my API"}), 200

### Code between this lines ###
if __name__ == '__main__':
    app.run()