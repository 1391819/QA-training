# will contain all configurations
from flask import Flask

app = Flask(__name__)

# needs to be after app instance to avoid circulation imports
import application.routes
