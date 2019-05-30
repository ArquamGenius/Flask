from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html");
@app.route("/contactus")
def cus():
	return render_template("Form.html");
@app.route("/formraginstration.php")
def phpreturn():
	return render_template("formraginstration.php");
@app.route("/about")
def aboutme():
	phone="7007030997";
	return render_template("About/about.html",Mobile=phone);

app.run(debug=True)


