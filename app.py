from flask import Flask, request, render_template

#creating application
app = Flask(__name__)

# to clear terminal : clear

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if (__name__) == "__main__":
    app.run()