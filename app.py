from flask import Flask
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def home():
    return "Bonjour DevOps 🚀 - version 1"

if __name__ == "__main__":
    app.run(debug=True)