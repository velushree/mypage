from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
import ssl

#
app = Flask(__name__)

client=MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.br4vj.mongodb.net/mydatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["mydatabase"]
collection=db["blog"]
collection1=db["contact"]
ismayil = db["adminpage"]

@app.route("/")
def Homepage():
    return render_template("Home.html")

@app.route("/general")
def next():
    return render_template("general.html")

@app.route("/blogview")
def blogview():
    allblog=collection.find()
    return render_template("blog_view.html",blogs=allblog)

@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        name=request.form.get('name')
        content=request.form.get('content')

        contact={
            "name":name,
            "content":content
        }
        collection1.insert_one(contact)
        return redirect("/general")
    else:
        return render_template("contact.html")
