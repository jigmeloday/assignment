from customer import *
from sales import *

def menu():
    print("1. Add a new customer")
    print("2. Add a new transaction")
    print("3. Search customers")
    print("4. Search sales transactions")
    print("5. Display sales transactions for a customer")
    print("6. Delete a transaction record")
    print("7. Delete a customer")
    print("8. Quit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        postcode = input("Enter postcode: ")
        phone = input("Enter phone number: ")
        customer = add_customer(name, postcode, phone)
        print(f"Customer ID: {customer.customer_id} added successfully.")

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
            print(f"Customer ID: {customer.customer_id}, Name: {customer.name}")

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
        break

    else:
        print("Invalid choice. Please try again.")