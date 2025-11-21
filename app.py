from flask import Flask, request, render_template

#creating application
app = Flask(__name__)

# to clear terminal : clear

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    return(render_template("main.html"))

if (__name__) == "__main__":
    app.run()

