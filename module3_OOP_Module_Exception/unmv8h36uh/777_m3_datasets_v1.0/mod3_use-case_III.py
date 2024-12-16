import re
import csv

# Define the Customer class
class Customer:
    def __init__(self, title, first_name, last_name, is_blacklisted):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.is_blacklisted = is_blacklisted

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} - Blacklisted: {self.is_blacklisted}"

# Define the Order class
class Order:
    def __init__(self, customer, product_name, product_code):
        self.customer = customer
        self.product_name = product_name
        self.product_code = product_code

    def __str__(self):
        return f"[+] --> Order for {self.customer.first_name} {self.customer.last_name}: {self.product_name} (Code: {self.product_code})"

# Define the custom exception
class CustomerNotAllowedException(Exception):
    def __init__(self, customer):
        self.customer = customer
        super().__init__(f"[-] --> Customer {customer.first_name} {customer.last_name} is blacklisted and not allowed to create an order.")

# Function to create order
def createOrder(customer, product_name, product_code):
    if customer.is_blacklisted:
        raise CustomerNotAllowedException(customer)
    return Order(customer, product_name, product_code)

# Function to parse title and first name using regular expressions
def parse_title_first_name(data):

    # Define the regular expression pattern
    pattern = re.compile(r'([^,]+),\s*([^,]+)\.\s*([^,]+),\s*([^,]+)')

    # Find all matches in the data
    matches = pattern.findall(data)

    # Print the matches
    if matches:
        for match in matches:
            last_name = match[0].strip()
            title = match[1].strip()
            first_name = match[2].strip()
            flag = match[3].strip()
            #print((last_name, title, first_name, flag))
            return last_name, title, first_name, flag
    else:
        print("No matches found")
        return None, None, None, None   

# Read CSV and process data
customers = []

# Open the file in read mode
with open('FairDealCustomerData.csv', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Process the line (e.g., print it)
        #print(line.strip())
        last_name, title, first_name, blacklisted = parse_title_first_name(line)
        if title and first_name:
            customer = Customer(title, first_name, last_name, bool(int(blacklisted)))
            customers.append(customer)
        else:
            print(f"Skipping invalid entry: {line}")

# Example usage
for customer in customers:
    print(customer)
    try:
        order = createOrder(customer, "SampleProduct", "SP123")
        print(order)
    except CustomerNotAllowedException as e:
        print(e)
