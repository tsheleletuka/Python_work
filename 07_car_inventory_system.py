def build_car(**car_info):
    return car_info

# Example call:
car1 = build_car(make="Toyota", model="Corolla", year=2022, color = "Blue")
print(car1)

# Create an empty inventory list
inventory = []

# Function to add cars to the inventory
def add_car_to_inventory(**car_info):
    car = build_car(**car_info)     # Build a car using the details
    inventory.append(car)       # Add the car to the inventory

# Add a few cars
add_car_to_inventory(make="Toyota", model="Corolla", year= 2022, color="Blue")
add_car_to_inventory(make="Honda", model="Civic", year= 2021, color="Grey")
add_car_to_inventory(make="Mazda", model="CX", year= 2020, color="Black")

# Function to display the inventory in a more readable format
def display_inventory():
    print("\nCar Inventory:")
    for car in inventory:
        print(f"\n{car['make']} {car['model']} ({car['year']}) - {car['color']}")
        

# Display the inventory
display_inventory()