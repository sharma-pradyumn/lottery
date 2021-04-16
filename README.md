# lottery
Flask API for a lottery draw. It uses Flask SQLAlchemy for database.

Details: 

/customers : Returns a json showing all customers. It also allows to add more customers by accepting a post request, with the customer details (customer name only as of now) in a json object.

/customers/winners : It shows all the past winners

/customers/draw : It is one raffle draw. It checks amongst all customers who have a raffle ticket and selects one winner and returns it as a json object.

/customers/set_ticket/<int:id> : For a customer with customer_id as id, it set a raffle ticket for the customer for the next upcoming draw

/customers/<int:id> : Shows all the details of the customer having customer_id as id and returns a  json object.
                     A 'PUT' request along with a json object can be used to update the details of any customer.
