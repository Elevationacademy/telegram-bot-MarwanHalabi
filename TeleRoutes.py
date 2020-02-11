from flask import Flask, request, Response
from funcs import *

app = Flask(__name__)


@app.route('/message', methods=["POST"])  # /check
def handle_message():
    global prime_lag
    print("got message")
    message = request.get_json()['message']
    check_func(message)
    fact_func(message)
    Palindrome_func(message)
    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
