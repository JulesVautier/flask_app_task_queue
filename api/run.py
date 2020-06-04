import os
import sys

from app.api import app_flask

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, "app"))

if __name__ == '__main__':
    app_flask.run(debug=True, host='0.0.0.0')
