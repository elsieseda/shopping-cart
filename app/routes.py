from flask import Flask, render_template, request
from datetime import datetime as dt
from .models import *
"""from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))"""

@app.route("/", methods=["POST"])
def index():
	title=request.form.get("title")
	image=request.form.get("image")
	price=request.form.get("price")
	description=request.form.get("description")

	posts=Post(title=title,image=image,price=price,description=description)
	db.session.add(posts)
	db.session.commit()
	"""db.execute("INSERT INTO posts("title","image","price","description"),{"title":title,"image":image,"price":price,"description":description}")
	db.commit()"""
	return render_template("index.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/shop")
def shop():
	"""posts=db.execute("SELECT * FROM posts LIMIT = 6").fetchall()"""
	return render_template("shop.html")

@app.route("/contact")
def contact():

	return render_template("contact.html")

@app.route("/login")
def login():
"""	users=db.execute("SELECT * FROM users WHERE email=:email AND password=:password",{"email":email,"password":password})
	"""	
	return render_template("login.html")

@app.route("/logout")
def logout():
	return render_template("logout.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/posts")
def posts():
	posts=Post.query.all()
	"""posts=db.execute("SELECT * FROM posts").fetchall()"""
	return render_template("posts.html")