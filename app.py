from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def receive_get_request():
    print("GET request")
    return "GET response"


@app.route("/", methods=['POST'])
def receive_post_request():
    print("POST request")
    return "POST response"


@app.route("/1", methods=['GET', 'POST'])
def receive_generic_request():
    if request.method == 'GET':
        print("GET response on /1")
        return "GET response on /1"
    else:
        print("POST response on /1")
        return "POST response on /1"


if __name__ == "__main__":
    app.run()
