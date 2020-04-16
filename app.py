  
from flask import Flask

# Create the application instance
app = Flask(__name__)


# Create a URL route in our Flask application for "/"
@app.route('/')
def home():
    return "Automation for the people"


# runs on port 5000 by default.
if __name__ == '__main__':
    print("Starting!")
    app.run(debug=False, host='0.0.0.0')