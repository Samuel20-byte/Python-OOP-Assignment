# constructors_and_destructors.py

class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} {self.model} has been created.")

    # Method
    def display(self):
        print(f"Car: {self.brand}, Model: {self.model}")

    # Destructor
    def __del__(self):
        print(f"{self.brand} {self.model} is being destroyed.")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("BMW", "X5")

# Use methods
car1.display()
car2.display()

# Delete object manually (optional)
del car1

print("End of program.")