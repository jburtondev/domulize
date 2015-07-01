from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Domulize '

if __name__ == '__main__':
    app.debug = True
    app.run()
