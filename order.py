class Order:
    orders = []

    def __init__(self, order_id, customer_id, bike_id, quantity, total_price, date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.bike_id = bike_id
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

    def generate_bill(self):
        print(f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, Bike ID: {self.bike_id}, Quantity: {self.quantity}, Total Price: {self.total_price}, Date: {self.date}")

    def confirm_order(self):
        Order.orders.append(self)
        print("Order confirmed!")

    def cancel_order(self):
        if self in Order.orders:
            Order.orders.remove(self)
            print("Order canceled!")
        else:
            print("Order not found!")
