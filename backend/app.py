from flask import Flask
from get_corona_data import get_data
app = Flask(__name__)

@app.route('/')
def homepage():
    return get_data()

if __name__ == "__main__":
    app.run()
