 
from flask import Flask

app = Flask(__name__ , template_folder="views")

app.secret_key = "75fc78df8vhj92gv92yvhz"

from application.controllers import *