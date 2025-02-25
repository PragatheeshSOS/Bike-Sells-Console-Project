class Payment:
    def __init__(self, order_id, method):
        self.order_id = order_id
        self.method = method
        self.status = "Pending"

    def process_payment(self):
        print(f"Processing payment for Order {self.order_id} via {self.method}...")
        confirmation = input("Confirm payment? (yes/no): ")
        if confirmation.lower() == 'yes':
            self.status = "Success"
            print("Payment successful!")
            return True
        else:
            self.status = "Failed"
            print("Payment cancelled!")
            return False
