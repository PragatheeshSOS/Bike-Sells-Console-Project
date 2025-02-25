class Bike:
    def __init__(self, bike_id, model, brand, price, engine_capacity, mileage, stock, status):
        self.bike_id = bike_id
        self.model = model
        self.brand = brand
        self.price = price
        self.engine_capacity = engine_capacity
        self.mileage = mileage
        self.stock = stock
        self.status = status

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.status = "Available" if self.stock > 0 else "Out of Stock"
            print(f"Stock updated. Remaining stock: {self.stock}")
        else:
            print("Not enough stock available!")

    def display_details(self):
        print(f"ID: {self.bike_id}, Model: {self.model}, Brand: {self.brand}, Price: {self.price}, Engine: {self.engine_capacity}, Mileage: {self.mileage}, Stock: {self.stock}, Status: {self.status}")

    def check_availability(self):
        return self.stock > 0
