#defining a class for restaurant:
class Restaurant:
    """an exercise for showing the situation of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """initializing the information of restaurant"""
        self.rest_name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        """printing the information of restaurant."""
        print(f"\nthe name of the restaurant is {self.rest_name} which provides {self.cuisine} foods.")
        
    def open_restaurant(self):
        """printing the situation of restaurant."""
        print(f"\nthe {self.rest_name} is open!!!")
        
    
#creating an instance and using it:
restaurant1 = Restaurant('pizza_Hot', 'fastfood')      
print(f'the {restaurant1.rest_name} is added to the class with a type of food as {restaurant1.cuisine}')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#creating other instances and using them:
restaurant2 = Restaurant('ghoreishi','kebab')
restaurant3 = Restaurant('miami','jigar')
restaurants_list = [restaurant1, restaurant2, restaurant3]
for item in restaurants_list:
    item.describe_restaurant()

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