from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/portfolio'
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    msg = db.Column(db.String(120), nullable=False)




@app.route("/")
def index():
	return render_template("index.html")

@app.route("/gallery")
def gallery():
	return render_template("gallery.html")

@app.route("/skills")
def skills():
	return render_template("skills.html")

@app.route("/contact", methods = ['GET','POST'])
def contact():

	if request.method=='POST':

		name = request.form.get('contact_name')
		email = request.form.get('contact_email')
		msg = request.form.get('contact_message')

		entry = Contact(name=name,email=email,msg=msg)

		db.session.add(entry)
		db.session.commit()

	return render_template("contact.html")



app.run(debug=True)