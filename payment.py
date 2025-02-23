class Payment:
    def __init__(self, payment_id, order_id, payment_method):
        self.payment_id = payment_id
        self.order_id = order_id
        self.payment_method = payment_method
        self.status = "None"
    
    def processPayment(self):
        print("Processing")

    def refundPayment(self):
        print("Refunded")

    def getPaymentStatus(self):
        print("Payment Status")