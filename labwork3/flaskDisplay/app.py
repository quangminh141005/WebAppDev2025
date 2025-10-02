from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/welcome")
def index():
    return render_template("index.html")

@app.route("/table")
def table():
    data = [
        {"name": "alice", "age": 22},
        {"name": "Bob", "age": 19},
        {"name": "Charlie", "age": 25},
        {"name": "David", "age": 24},
        {"name": "Eve", "age": 21}
    ]
    return render_template("table.html", data=data)

@app.route("/factorial/<int:num>")
def num_factorial(num):
    return render_template("factorial.html", data=math.factorial(num))

@app.route("/is_prime/<int:num>")
def check_prime(num):
    def is_prime(num):
        if num <= 1:
            return "Not Prime"
        if num == 2:
            return "Prime"
        if num % 2 == 0:
            return "Not Prime"
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return "Not Prime"
        return "Prime"

    return render_template("checkPrime.html", data=is_prime(num))
        
@app.route("/sort")
def sort():
    arr = request.args.get("number")
    numbers = [int(num.strip()) for num in arr.split(",") if num.strip()]
    numbers.sort()
    return render_template("sortArray.html", data=numbers)

@app.route("/reverse_string/<string:arr>")
def reverse(arr):
    arr = [char for char in arr]
    arr = arr[::-1]
    sentence = "".join(arr)
    return render_template("reverseString.html", data=sentence)
