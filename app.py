from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/streamlit", methods=["GET", "POST"])
def run_streamlit():
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
    return "Streamlit is running!"

if __name__ == "__main__":
    app.run(debug=True)
