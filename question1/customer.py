class Customer:
    def __init__(self, customer_id, name, postcode="", phone=""):
        self.customer_id = customer_id
        self.name = name
        self.postcode = postcode
        self.phone = phone

customer_records = []

def add_customer(name, postcode="", phone=""):
    customer_id = len(customer_records) + 1
    customer = Customer(customer_id, name, postcode, phone)
    customer_records.append(customer)
    return customer

def search_customers(search_string):
    search_string = search_string.lower()
    matching_customers = [customer for customer in customer_records if search_string in customer.name.lower()]
    return matching_customers

def delete_customer(customer_id):
    global customer_records
    customer_records = [customer for customer in customer_records if customer.customer_id != customer_id]