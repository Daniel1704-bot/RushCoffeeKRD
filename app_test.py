from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print("Current dir:", os.getcwd())
    print("Template folder:", app.template_folder)
    print("Index exists:", os.path.exists('templates/index.html'))
    app.run(debug=True, port=5000)