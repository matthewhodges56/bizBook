from flask import Blueprint, request, jsonify
from models.user import authenticate_user

# Create the Blueprint for auth-related routes
auth_bp = Blueprint('auth', __name__)

# A simple auth route (no authentication for now)
@auth_bp.route('/check_user', methods=['POST'])
def check_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if authenticate_user(email, password):
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401 #401 is unauthorized.