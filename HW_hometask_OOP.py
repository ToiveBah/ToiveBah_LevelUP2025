#Stage 1. Base class
class Drink:
    
    def __init__(self, name, volume):
        self.name = name  #drink name
        self.volume = volume  #volume in milliliters

    def display_info(self):
        return f" {self.name} объемом {self.volume} мл\n"

#Stage 2. Inheritance and polymorphism
class HotDrink(Drink):  #for hot drinks
    
    def __init__(self, name, volume, temperature=75):
        super().__init__(name, volume)
        self.temperature = temperature  #temperature in degrees Celsius

    def display_info(self):
        return f" {self.name} объемом {self.volume} мл и температурой {self.temperature}°C\n"

class ColdDrink(Drink): #for cold drinks
    
    def __init__(self, name, volume, ice_cubes=3):
        super().__init__(name, volume)
        self.ice_cubes = ice_cubes  #number of ice cubes

    def display_info(self):
        return f" {self.name} объемом {self.volume} мл и {self.ice_cubes} кубильков льда\n"

#Stage 3. Interaction of objects
class Customer():  #describes a cafe customer
    
    def __init__(self, name, orders):
        self.name = name  #client's name
        self.orders = []  #list of ordered drinks
        
    def order_drink(self, drink):  #adds a drink to the customer's orders
        self.orders.append(drink)
     
    def show_orders(self):  #displays a list of customer orders with information about each drink
        details = " ".join(d.display_info() for d in self.orders)
        return f"Клиент {self.name} заказал:\n {details}"
    
#Stage 4. Cafe menu
class DrinkMenu():  #stores available drinks
    
    def __init__(self, drinks):
        self.drinks = drinks  #list of beverage items
        
    def add_drink(self, drink):  #adds a drink to the menu
        self.drinks.append(drink)
        
    def show_all_drinks(self):   #displays all drinks on the menu
        details = " ".join(d.display_info() for d in self.drinks)
        return f"В меню представлены:\n {details}"


#Stage 5. Checking Interaction
#1. Creat multiple drink objects of different types
drink_1 = Drink(name="Мохито", volume=200)   
drink_2 = HotDrink(name="Чай", volume=500, temperature=90)   
drink_3 = ColdDrink(name="Сок", volume=350, ice_cubes=5)   
drink_4 = Drink(name="Пина Колада", volume=200)
drink_5 = HotDrink(name="Кофе", volume=150)

#2. Add drinks to the cafe menu
menu = DrinkMenu([drink_1, drink_2, drink_3, drink_4, drink_5]) 

#3. Create a customer who will order from the menu
client_1 = Customer(name="Надежда", orders=[])
client_1.order_drink(drink_2)
client_1.order_drink(drink_5)

#4. Displays on the screen: current menu, customer orders
print(menu.show_all_drinks())
print(client_1.show_orders())