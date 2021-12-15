from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "prueba  flask"

if __name__=="__main__":
    app.run(port=3000, debug= True)