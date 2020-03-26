from flask import Flask, render_template
import os
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

#print(os.environ.get("SECRET_KEY"))
app.secret_key = "test"

@app.route('/')
def home():
    return render_template('hello.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)