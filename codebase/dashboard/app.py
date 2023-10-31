from flask import Flask, render_template

# Initialise the Flask app
app = Flask(__name__)
app.secret_key = 'ADD SECRET KEY HERE'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()