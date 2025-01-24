import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print(f"Templates folder: {os.path.abspath(app.template_folder)}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
