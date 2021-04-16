'''
TODO : Reset ticket after each draw
'''

from customer_info import *


# route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    '''Function to get all the customers in the database'''
    ''' Returns a list of customers'''
    return jsonify({'Customers': Customer.get_all_customers()})

#route to draw one random as winner
@app.route('/customers/draw', methods=['GET'])
def get_random_customers():
    '''Function to get a random winner among the customers in the database'''
    ''' Returns a customer'''
    return jsonify({'Winner': Customer.get_random_customer()})

@app.route('/customers/winners',methods=['GET'])
def get_winners():
    return jsonify({'Winners': Winner.get_all_winner()})


# route to get customer by id
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    return_value = Customer.get_customer(id)
    return jsonify(return_value)

@app.route('/customers/set_ticket/<int:id>', methods=['GET'])
def set_customer_ticket_by_id(id):
    Customer.set_ticket(id)
    response = Response("Ticket set for "+str(id), 201, mimetype='application/json')
    return response


# route to add new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    '''Function to add new customer to our database'''
    request_data = request.get_json()  # getting data from client
    Customer.add_customer(request_data["name"], request_data["ticket"])
    response = Response("Customer added", 201, mimetype='application/json')
    return response

# route to update customer with PUT method
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    '''Function to edit customer in our database using customer id'''
    request_data = request.get_json()
    Customer.update_customer(id, request_data['name'], request_data['ticket'])
    response = Response("Customer Updated", status=200, mimetype='application/json')
    return response

# # route to delete customer using the DELETE method
# @app.route('/customers/<int:id>', methods=['DELETE'])
# def remove_customer(id):
#     '''Function to delete customer from our database'''
#     Customer.delete_customer(id)
#     response = Response("Customer Deleted", status=200, mimetype='application/json')
#     return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)