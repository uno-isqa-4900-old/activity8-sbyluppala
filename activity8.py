import csv


class Customer:

    # stores customer data wih attributes ID, first name, last name, company, address, city, state, zip.
    def __init__(self, ID=0, firstName='', lastName='', company='', address='', city='', state='', zipcode=''):
        self.ID = str(ID)
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # method that returns details of the customer.
    def getDetails(self):
        if self.company != "":
            return str(self.firstName) + " " + str(self.lastName) + "\n" + str(self.company) + "\n" + self.address +\
                   "\n" + self.city + ", " + self.state + " " + str(self.zipcode)
        if self.company == "":
            return str(self.firstName) + " " + str(self.lastName) + "\n" + self.address + "\n" + self.city \
                   + ", " + self.state + " " + str(self.zipcode)
        pass


def display_title():
    print("Customer Viewer")
    pass


filename = 'customers.csv'


# reads CSV and stores the data
def csv_reader(self):
    with open(filename, newline="") as csvfile:
        custlist = []
        custreader = csv.DictReader(csvfile)
        for row in custreader:
            customer = Customer(row['cust_id'], row['first_name'], row['last_name'], row['company_name'],
                                row['address'], row['city'], row['state'], row['zip'])
            custlist.append(customer)
    return custlist
    pass


# searches for the required customer and displays details
def find_customer(cust_id):
    customers = csv_reader(Customer)
    message = 'No customer with that specified ID.'
    if str(cust_id) == '':
        return message
    elif 101 <= int(cust_id) <= 600:
        customer_id = customers[int(cust_id) - 101]
        print(customer_id.getDetails())
        return customer_id

    elif cust_id == ' ':
        print(message)
        return message
    else:
        print(message)
        return message
    pass


def main():
    display_title()
    response = 'y'
    while response.lower() == 'y':
        cust_id = input("\nEnter Customer ID: ")
        # function to read csv file and search for ID
        find_customer(str(cust_id))
        # response to either continue or not
        response = input("\nContinue? (y/n): ")
        if response.lower() != 'y' and response.lower() != 'n':
            print("Please enter a valid response (y/n)")
            response = input("\nContinue? (y/n): ")
        elif response.lower() == 'n':
            print("Bye!")
            break


if __name__ == '__main__':
    main()





