from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "prueba  flask"

@app.route("/edit_user")
def edit_user():
    return "editar usuario"

@app.route("/add_user")
def add_user():
    return "Añadir usuario"

@app.route("/delete_user")
def delete_user():
    return "Eliminar usuario"
    
if __name__=="__main__":
    app.run(port=3000, debug= True)