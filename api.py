from customer_info import *
import datetime 
import random

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

@app.route('/customers/set_ticket', methods=['POST'])
def set_customer_ticket_by_id():
    request_data = request.get_json()
    id=request_data['id']
    Customer.set_ticket(id)
    response = Response("Ticket set for "+str(id), 201, mimetype='application/json')
    return response


# route to add new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    '''Function to add new customer to our database'''
    request_data = request.get_json()  # getting data from client
    if (request_data is None):
        response = Response("Please send data of customer to add in JSON", 201, mimetype='application/json')
        return response
    Customer.add_customer(request_data["name"],0)
    response = Response("Customer added", 201, mimetype='application/json')
    return response

# route to update customer with PUT method
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    '''Function to edit customer in our database using customer id'''
    request_data = request.get_json()
    if (request_data is None):
        response = Response("Please send details of customer to update in JSON", 201, mimetype='application/json')
        return response
    Customer.update_customer(id, request_data['name'], request_data['ticket'])
    response = Response("Customer Updated", status=200, mimetype='application/json')
    return response

@app.route('/customers/next_draw', methods=['GET'])
def next_draw():
    '''Returns tommorows date and 10 AM as the next draw time '''
    tommorow=datetime.date.today()+datetime.timedelta(days = 1)
    tommorow=tommorow.strftime('%d-%m-%Y')+" at 10 AM" 
    return jsonify({'Next Draw':tommorow})

@app.route('/customers/next_reward', methods=['GET'])
def next_reward():
    '''Returns tommorows reward. Reward is chosen randomly from a list of
        potential records.
     '''

    rewards=['Washing Machine','Mobile Phone','Electric Kettle']
    return jsonify({'Next Reward':random.choices(rewards)})
    

# # route to delete customer using the DELETE method
# @app.route('/customers/<int:id>', methods=['DELETE'])
# def remove_customer(id):
#     '''Function to delete customer from our database'''
#     Customer.delete_customer(id)
#     response = Response("Customer Deleted", status=200, mimetype='application/json')
#     return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)