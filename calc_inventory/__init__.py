from flask import Flask, render_template, request, redirect
from .classes import Calculator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html", display="")

@app.route("/calculate", methods = ["POST"])
def calculate():
    if request.method == "POST":
        try:
            form = request.form
            num1 = float(form['num1'])
            num2 = float(form['num2'])
            arithmetic = Calculator(num1, num2)
            if form["submit_button"] == "add":
                return render_template('base.html', display=arithmetic.add_the_numbers())
            elif form["submit_button"] == "subtract":
                return render_template('base.html', display=arithmetic.subtract_the_numbers())
            elif form["submit_button"] == "multiply":
                return render_template('base.html', display=arithmetic.multiply_the_numbers())
            elif form["submit_button"] == "divide":
                return render_template('base.html', display=arithmetic.divide_the_numbers())
        except:
            return render_template('base.html', display="Enter Valid Numbers and Try Again")
        
    return redirect("/")


