from . import db

class Post(db.Model):
	__tablename__="posts"
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String,nullable=False)
	image=db.Column(db.String,nullable=False)
	price=db.Column(db.Integer,nullable=False)
	description=db.Column(db.String,nullable=False)
	created = db.Column(db.DateTime, nullable=False)

class Contact(db.Model):
	__tablename__="contacts"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String,nullable=False)
	email=db.Column(db.String,nullable=False)
	subject=db.Column(db.String,nullable=False)
	message=db.Column(db.String,nullable=False)



	
		


"""class Item:
	def __init__(self, id, name, price=0, quantity=1):
		self.id= id
		self.name= name
		self.price=price
		self.quantity=quantity

class Cart:
	def __init__(self):
		self.content=dict()

	def add_item():
		if item.id not in content:
			

	def total():

	def num_items():

	def remove_item():
"""