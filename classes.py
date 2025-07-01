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
    
    
    
#creating an instance and using it:
restaurant1 = Restaurant('pizza_Hot', 'fast food')      
print(f'the {restaurant1.rest_name} is added to the class with a type of food as {restaurant1.cuisine}')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#creating other instances and using them:
restaurant2 = Restaurant('ghoreishi','kebab')
restaurant3 = Restaurant('miami','jigar')
restaurants_list = [restaurant1, restaurant2, restaurant3]
for item in restaurants_list:
    item.describe_restaurant()

#utilizing serve attribute and modify that directly:
restaurant4 = Restaurant('meykhosh', 'caesar salad')
restaurant4.number_served = 25
restaurant4.show_served_number()

#use a method to modify served number:
restaurant4.set_served_number(20)
restaurant4.show_served_number()

#use a method in increase the number of serves:
restaurant4.increment_served_number(15)
restaurant4.show_served_number()

#creating Icecream stand class:
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
        
# creating an instance for ice cream stand restaurant:
restaurant5 = IceCreamStand('nemat','ice cream')
restaurant5.describe_restaurant()
restaurant5.flavor_describe()
    


#creating user class:
class User:
    """a class for talking with users"""
    def __init__(self, first_name, last_name, age, city):
        self.f_name = first_name
        self.l_name = last_name
        self.full_name = first_name +" " + last_name
        self.user_age = age
        self.user_city = city
        self.year = 2025-age

    def describe_user(self):
        print(f'the users first name is {self.f_name} and the last name is {self.l_name}.'
              f'the user is {self.user_age} year old and was born on {self.year} in {self.user_city}')
        
    def greeting_user(self):
        print(f'welcome to program {self.full_name}.')
        
user1 = User('jami','mashallah',23,'toorghoozabad')
user1.describe_user()
user1.greeting_user()

#creating administrator class:
class Admin(User):
    """a class for admins"""
    def __init__(self, first_name, last_name, age, city):
        """initiating admin"""
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def adding_right(self, new_right):
        "for adding the other rights of admin"
        self.privileges.append(new_right)
        
    def show_privileges(self):
        print(f'the {self.f_name} has the rights below:')
        for right in self.privileges:
            print(f'-{right}')
            
#creating an admin instance:
user2 = Admin('Reza', 'jafari', 25 , 'tehran')
user2.adding_right('ordering pizza by the visa card of user3')
user2.describe_user()
user2.show_privileges()
        
