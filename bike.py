class Bike:
    def __init__(self,bikeID,model,brand,price,engine_cap,stock,status):
        self.bikeID = bikeID
        self.model = model
        self.brand = brand
        self.price = price
        self.engine_cap = engine_cap
        self.stock = stock
        self.status = status
    
    def displayDetails(self):
        print(f"Bike ID: {self.bikeID}\nBike Model: {self.model}\nBrand: {self.brand}\nPrice: {self.price}\nEngine Capacity: {self.engine_cap}\nStock: {self.stock}\nStatus: {self.status}")

    def updateStock(self, quantity):
        print("Stock Updated")
        
    def checkAvailability(self):
        print("Availability")