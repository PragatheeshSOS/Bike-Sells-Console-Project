from main import customers
class Customer:
    def __init__(self, customer_id, name, contact, email, password):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact
        self.email = email
        self.password = password
    
    def register(self):
        print("Registered Successfully")
    
    @staticmethod
    def login(email, password):
        for customer in customers:
            if customer.email == email and customer.password == password:
                print("Login successful!")
                return True
        print("Invalid credentials! Try again.")
        return False
    def viewBikes(self):
        print("Display")

    def placeOrder(self):
        print("Place Order")