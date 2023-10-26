import csv
from customer_module import *
from sales import *

def load_customer_records_from_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer_id = int(row['customer_id'])
            if not any(cust.customer_id == customer_id for cust in customer_records):
                name = row['name']
                postcode = row['postcode']
                phone = row['phone']
                add_customer(name, postcode, phone)

def save_customer_records_to_file(file_path):
    if file_path.endswith('.csv'):
        write_mode = 'w'
    else:
        file_path += '.csv'
        write_mode = 'w'
    
    with open(file_path, write_mode, newline='') as csvfile:
        fieldnames = ['customer_id', 'name', 'postcode', 'phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for customer in customer_records:
            writer.writerow({'customer_id': customer.customer_id, 'name': customer.name, 'postcode': customer.postcode, 'phone': customer.phone})

def load_transaction_records_from_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer_id = int(row['customer_id'])
            if any(cust.customer_id == customer_id for cust in customer_records):
                date = row['date']
                category = row['category']
                value = float(row['value'])
                add_transaction(customer_id, date, category, value)

def save_transaction_records_to_file(file_path):
    if file_path.endswith('.csv'):
        write_mode = 'w'
    else:
        file_path += '.csv'
        write_mode = 'w'
    
    with open(file_path, write_mode, newline='') as csvfile:
        fieldnames = ['transaction_id', 'customer_id', 'date', 'category', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in sales_transactions:
            writer.writerow({'transaction_id': transaction.transaction_id, 'customer_id': transaction.customer_id, 'date': transaction.date, 'category': transaction.category, 'value': transaction.value})

while True:
    print("Menu:")
    print("1. Add a new customer")
    print("2. Add a new transaction")
    print("3. Search customers")
    print("4. Search sales transactions")
    print("5. Display sales transactions for a customer")
    print("6. Delete a transaction record")
    print("7. Delete a customer")
    print("8. Load customer records from a CSV file")
    print("9. Save all customer records to a CSV file")
    print("10. Load transaction records from a CSV file")
    print("11. Save all transaction records to a CSV file")
    print("12. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
       name = input("Enter customer name: ")
       postcode = input("Enter postcode: ")
       phone = input("Enter phone number: ")
       customer_module = add_customer(name, postcode, phone)
       print(f"Customer ID: {customer_module.customer_id} added successfully.")
    elif choice == "2":
       customer_id = int(input("Enter customer ID: "))
       date = input("Enter transaction date: ")
       category = input("Enter transaction category: ")
       transaction = add_transaction(customer_id, date, category)
       print(f"Transaction ID: {transaction.transaction_id} added successfully.")

    elif choice == "3":
        search_string = input("Enter search string: ")
        matching_customers = search_customers(search_string)
        for customer in matching_customers:
            print(f"Customer ID: {customer_module.customer_id}, Name: {customer.name}")
    elif choice == "4":
        search_string = input("Enter search string: ")
        matching_transactions = search_transactions(search_string)
        for transaction in matching_transactions:
            print(f"Transaction ID: {transaction.transaction_id}, Category: {transaction.category}")

    elif choice == "5":
        customer_id = int(input("Enter customer ID: "))
        customer_transactions = get_transactions_by_customer(customer_id)
        for transaction in customer_transactions:
            print(f"Transaction ID: {transaction.transaction_id}, Category: {transaction.category}")

    elif choice == "6":
        transaction_id = int(input("Enter transaction ID to delete: "))
        delete_transaction(transaction_id)
        print("Transaction deleted successfully.")

    elif choice == "7":
        customer_id = int(input("Enter customer ID to delete: "))
        delete_customer(customer_id)
        print("Customer and associated transactions deleted successfully.")

    elif choice == "8":
        file_path = input("Enter the path of the CSV file to load customer records from: ")
        load_customer_records_from_file(file_path)
        print("Customer records loaded successfully.")

    elif choice == "9":
        file_path = input("Enter the path of the CSV file to save customer records to: ")
        save_customer_records_to_file(file_path)
        print("Customer records saved successfully.")

    elif choice == "10":
        file_path = input("Enter the path of the CSV file to load transaction records from: ")
        load_transaction_records_from_file(file_path)
        print("Transaction records loaded successfully.")

    elif choice == "11":
        file_path = input("Enter the path of the CSV file to save transaction records to: ")
        save_transaction_records_to_file(file_path)
        print("Transaction records saved successfully.")

    elif choice == "12":
        break

    else:
        print("Invalid choice. Please try again.")