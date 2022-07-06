from flask import Flask, Response
from flask import request

app = Flask ("New app")

@app.route("/")
def main_page():
    return "Main page"

@app.route("/hello")
def hello():
    return "Hi I am a new app."

@app.route("/workers", methods=["POST"])
def workers():
    return workers
    
@app.route("/worker", methods=["GET"])
def worker():
    workers.append({"age": request.form.get("name"),
                    "id": request.form.get("id")})
    return Response("Status was updated", status=201)


if __name__ == '__main__':
      app.run(debug=True, port=5000)
