# lottery
Flask API for a lottery draw. It uses Flask SQLAlchemy for database.

Details: 

/customers : Returns a json showing all customers. It also allows to add more customers by accepting a post request, with the customer details (customer name only as of now) in a json object.

/customers/winners : It shows all the past winners

/customers/draw : It is one raffle draw. It checks amongst all customers who have a raffle ticket and selects one winner and returns it as a json object.

/customers/set_ticket/<int:id> : For a customer with customer_id as id, it set a raffle ticket for the customer for the next upcoming draw

/customers/<int:id> : Shows all the details of the customer having customer_id as id and returns a  json object.
                     A 'PUT' request along with a json object can be used to update the details of any customer.


For example: After starting api.py, 

posting a get request to http://127.0.0.1:1234/customers displays all customers as a JSON object.It shows the details such as name, id, and ticket . Ticket indicate if they are eligible for the next raffle.

Posting a post request to http://127.0.0.1:1234/customers with a JSON object {"name":"Rahul"} adds a customer with the name Rahul. By default, a customer has a ticket=0, ie not eligible for the next draw.

To update the customer details of a customer having id as customer id as cust_id, a put request to http://127.0.0.1:1234/customers/cust_id is sent, with a JSON object, containg the updated name and ticket. For example, a put reequest with a JSON object {"name":"rahu","ticket":1} to http://127.0.0.1:1234/customers/4 updates the name and ticket of the customer with id=4 to Rahul and ticket as 1.

To make a customer eligible for the next raffle, we need to set the ticket for the custmoer. To add a ticket for a customer having customer id as cust_id, a get request to http://127.0.0.1:1234/c/customers/set_ticket/cust_id sets the ticket for the customer.

To make a lucky draw, a get request to http://127.0.0.1:1234//customers/draw returns the details of the winner customer and resets the tickets for all customers.

To view past winners, a get request to http://127.0.0.1:1234/customers/winners returns the deatils of all the past winners as a JSON object.


