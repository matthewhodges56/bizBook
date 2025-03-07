from flask import Blueprint, render_template

# Create the Blueprint for auth-related routes
login_bp = Blueprint('login', __name__)

# A simple login route (no authentication for now)
@login_bp.route('/login')
def login():
    return render_template('login.html')  # We'll create this login.html file next
