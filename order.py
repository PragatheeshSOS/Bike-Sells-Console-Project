class Order:
    def __init__(self, order_id, customer_id, bike_id, quantity, total_price, date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.bike_id = bike_id
        self.quantity = quantity
        self.total_price = total_price
        self.date = date
        
    def generateBill(self):
        print("Bill")

    def confirmOrder(self):
        print("Order Confirmed")

    def cancelOrder(self, bikes):
        print("Order Cancelled")