# Put your app in here.
from flask import Flask, request

app = Flask(__name__)


@app.get("/math/<operator>")
def math_result(operator):

    a = request.args.get("a")
    b = request.args.get("b")

    math_ftn = OPERATORS.get(operator)

    return math_ftn(a, b)


def add(a, b):
    """ add a and b param """

    return f"{int(a) + int(b)}"


def subtract(a, b):
    """ subtracts a and b param"""

    return f"{int(a) - int(b)}"


def multiply(a, b):
    """ multiplies a and b param"""

    return f"{int(a) * int(b)}"


def divide(a, b):
    """ divides a and b param"""

    return f"{int(a) / int(b)}"


OPERATORS = {
    "add": add,
    "sub": subtract,
    "mult": multiply,
    "div": divide
}
