from settings import *
import json
import random 
db=SQLAlchemy(app)

''' We created a seperate database for winners because it is possible that the past winners have discontinued the services 
	and thus have been removed from the database
'''

# A class for the past winners
class Winner(db.Model):
	__tablename__ = 'winner'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)

	def add_winner(_name):
		new_winner=Winner(name=_name)
		db.session.add(new_winner)
		db.session.commit()

	def json(self):
		return {'id': self.id, 'Name': self.name}
	    # this method we are defining will convert our output to json

	'''Shows all past winners'''
	def get_all_winner():
		return [Winner.json(winner) for winner in Winner.query.all()]




# the class Customer will inherit the db.Model of SQLAlchemy
class Customer(db.Model):
	__tablename__ = 'customer'  # creating a table name
	id = db.Column(db.Integer, primary_key=True)  # this is the primary key
	name = db.Column(db.String(80), nullable=False)
	# nullable is false so the column can't be empty
	ticket = db.Column(db.Integer, nullable=False)
	
	def json(self):
		return {'id': self.id, 'Name': self.name,
		'ticket': self.ticket}
	    # this method we are defining will convert our output to json

	def add_customer(_name, _ticket):
		'''function to add customer to database using _name, _ticket as parameters'''
		# creating an instance of our Customer constructor
		new_customer = Customer(name=_name,ticket=_ticket)
		db.session.add(new_customer)  # add new customer to database session
		db.session.commit()  # commit changes to session

	def get_all_customers():
		'''function to get all customers in our database'''
		return [Customer.json(customer) for customer in Customer.query.all()]

	def get_random_customer():
		eligible_customers=Customer.query.filter_by(ticket=1)
		if len((list(eligible_customers)))==0:
			return "No customer had a ticket"
		winner_customer=random.choice(list(eligible_customers))
		winner_name=winner_customer.name
		Winner.add_winner(winner_name)
		# remove raffle for all customers
		for cust in eligible_customers:
			cust.ticket=0
		db.session.commit()
		return Customer.json(winner_customer)



	def get_customer(_id):
		'''function to get customer using the id of the customer as parameter'''
		query=Customer.query.filter_by(id=_id).first()
		if (query is None):
			return "No customer of given id was found"
		return [Customer.json(query)]

		# Customer.json() coverts our output to the json format defined earlier
		# the filter_by method filters the query by the id
		# since our id is unique we will only get one result
		# the .first() method will get that first value returned

	def update_customer(_id, _name, _ticket):
		'''function to update the details of a customer using the id, name,
		ticket and genre as parameters'''
		customer_to_update = Customer.query.filter_by(id=_id).first()
		customer_to_update.name = _name
		customer_to_update.ticket = _ticket
		db.session.commit()

	def set_ticket(_id):
		customer_to_update = Customer.query.filter_by(id=_id).first()
		customer_to_update.ticket = 1
		db.session.commit()


	def delete_customer(_id):
		'''function to delete a customer from our database using
		   the id of the customer as a parameter'''
		Customer.query.filter_by(id=_id).delete()
		# filter customer by id and delete
		db.session.commit()  # commiting the new change to our database



