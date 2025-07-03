import user_module

admin1 = user_module.Admin('reza', 'jafari', 25, 'tehran')
admin1.describe_user()
admin1.greeting_user()
admin1.adding_right('he can ask for 2 slices of pizza from you')
admin1.show_privileges()

