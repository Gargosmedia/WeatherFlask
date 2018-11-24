
from flask import Flask, request, render_template

readings={"10/1/1998":[20, "70%","Yes"], "10/2/1998":[30,"70%","Yes"]}


app = Flask(__name__)

@app.route("/")
def index():
    return "Station Works!"

@app.route("/command/<string:cmd>/")
def command(cmd):
    return render_template('template.html', cmd=cmd)

@app.route("/db/")
def db():
    return render_template('db.html', dict=readings)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
