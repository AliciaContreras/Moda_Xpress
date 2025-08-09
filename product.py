class Product:
    def __init__(self, name:str, price:str, quantity:str, size:str):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.size=size
    def __str__(self):
        return f"{self.name} - {self.price} - {self.quantity} - {self.size}"
    def display_details(self):
        print(self)