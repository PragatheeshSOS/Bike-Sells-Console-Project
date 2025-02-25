from datetime import datetime
from payment import Payment

class Order:
    orders = []
    next_id = 1
    
    def __init__(self, customer_id, bike, quantity):
        self.order_id = Order.next_id
        self.customer_id = customer_id
        self.bike = bike
        self.quantity = quantity
        self.total_price = bike.price * quantity
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if bike.stock >= quantity:
            bike.stock -= quantity
            bike.status = "Available" if bike.stock > 0 else "Out of Stock"
            Order.orders.append(self)
            Order.next_id += 1

            payment = Payment(self.order_id, "Card")
            if payment.process_payment():
                print(f"Order {self.order_id} placed successfully! Payment confirmed.")
            else:
                print("Payment failed! Order not confirmed.")
                Order.orders.remove(self)
                bike.stock += quantity
        else:
            print("Not enough stock available!")
