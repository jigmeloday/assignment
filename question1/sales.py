class SalesTransaction:
    def __init__(self, transaction_id, customer_id, date, category):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.date = date
        self.category = category
sales_transactions = []

def add_transaction(customer_id, date, category):
    transaction_id = len(sales_transactions) + 1
    transaction = SalesTransaction(transaction_id, customer_id, date, category)
    sales_transactions.append(transaction)
    return transaction

def search_transactions(search_string):
    search_string = search_string.lower()
    matching_transactions = [transaction for transaction in sales_transactions if
                             search_string in str(transaction.transaction_id).lower() or
                             search_string in str(transaction.date).lower() or
                              search_string in str(transaction.value).lower() or
                             search_string in transaction.category.lower()]
    return matching_transactions

def delete_transaction(transaction_id):
    global sales_transactions
    sales_transactions = [transaction for transaction in sales_transactions if transaction.transaction_id != transaction_id]

def get_transactions_by_customer(customer_id):
    return [transaction for transaction in sales_transactions if transaction.customer_id == customer_id]
