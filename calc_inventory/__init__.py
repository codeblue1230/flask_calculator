from flask import Flask, render_template, request, redirect
from .classes import addition, subtraction, multiplication, division

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
            if form["submit_button"] == "add":
                add_nums = addition(num1, num2)
                return render_template('base.html', display=add_nums.add_the_numbers())
            elif form["submit_button"] == "subtract":
                subtract_nums = subtraction(num1, num2)
                return render_template('base.html', display=subtract_nums.subtract_the_numbers())
            elif form["submit_button"] == "multiply":
                multiply_nums = multiplication(num1, num2)
                return render_template('base.html', display=multiply_nums.multiply_the_numbers())
            elif form["submit_button"] == "divide":
                divide_nums = division(num1, num2)
                return render_template('base.html', display=divide_nums.divide_the_numbers())
        except:
            return render_template('base.html', display="Enter Valid Numbers and Try Again")
        
    return redirect("/")


