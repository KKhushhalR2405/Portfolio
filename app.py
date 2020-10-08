from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/gallery")
def gallery():
	return render_template("gallery.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")



app.run(debug=True)