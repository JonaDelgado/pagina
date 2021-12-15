from flask import Flask, render_template

app = Flask(__name__)

posts=["hola","chao",2]


@app.route("/")
def index():
    return render_template("index.html",num_posts=len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("index.html", slug_title=slug)
    



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