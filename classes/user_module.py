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