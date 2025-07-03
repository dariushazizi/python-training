#defining a class for restaurant:
class Restaurant:
    """an exercise for showing the situation of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """initializing the information of restaurant"""
        self.rest_name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """printing the information of restaurant."""
        print(f"\nthe name of the restaurant is {self.rest_name} which provides {self.cuisine} foods.")
        
    def open_restaurant(self):
        """printing the situation of restaurant."""
        print(f"\nthe {self.rest_name} is open!!!")
        
    def show_served_number(self):
        """show the number of served food in the restaurant"""
        print(f"\n\tthe {self.rest_name} restaurant already served {self.number_served} of {self.cuisine} dishes.\n")
        
    def set_served_number(self, serv_num):
        """increase the served number by this method"""
        self.number_served = serv_num
    
    def increment_served_number(self, increment_num):
        self.number_served += increment_num
        
        

class IceCreamStand(Restaurant):
    """represent a specific kind of restaurant"""
    def __init__(self,  restaurant_name, cuisine_type, *flavors):
        """initialize the restaurant"""
        super().__init__( restaurant_name, cuisine_type)
        if flavors:
            self.flavors = list(flavors)
        else:
            self.flavors = ['vanilla', 'chocolate','mixed']
            
        
    def flavor_describe(self):
        """shows different kind of ice cream flavors"""
        print(f'Ice cream flavors are:')
        for item in self.flavors:
            print(item)