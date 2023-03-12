from flask import Flask, render_template, request, url_for
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        firstNum = request.form.get("numOne")
        secondNum = request.form.get("numTwo")

        ratio = calc_ratio(int(firstNum), int(secondNum))
        return render_template("home.html", ratio=ratio, success=None)

    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


def calc_ratio(a, b):
    gcd = math.gcd(a, b)
    ratio = [int(a / gcd), int(b / gcd)]
    return {"firstNum": abs(ratio[0]), "secondNum": abs(ratio[1])}


if __name__ == "__main__":
    home()
