#Project Flask MVC

from application import app
from flask_login import LoginManager




if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)