from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Personal Finance Management App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)  # Using port 5500 to avoid conflicts
