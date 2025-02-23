class Customer:
    def __init__(self, customer_id, name, contact, email, password):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact
        self.email = email
        self.password = password
    
    def register(self):
        print("Registered Successfully")
    
    def login(self):
        print("Login")

    def viewBikes(self):
        print("Display")

    def placeOrder(self):
        print("Place Order")