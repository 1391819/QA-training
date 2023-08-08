from flask import Flask
from dotenv import load_dotenv
import os

# creating Flask instance
app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# importing view functions after Flask instance creation
from application import routes
