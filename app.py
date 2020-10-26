import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def fib():
    seq = [0, 1]
    for i in range(1, 50-1):
        seq.append(seq[i-1] + seq[i])
    return str(seq)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
