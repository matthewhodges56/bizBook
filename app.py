from flask import Flask, render_template
import mysql.connector
from config import Config
from routes.login import login_bp 
from routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints 
app.register_blueprint(login_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
