from flask import Flask, render_template, request
from ai import ask_ai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""

    if request.method == "POST":
        question = request.form["question"]
        reply = ask_ai(question)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)