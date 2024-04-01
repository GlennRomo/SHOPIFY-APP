"""
Shopify App - Foundations: Programming Refresher Assignment

"""

class User_type:
    def __init__(self, type_name, user_rights):
        self.type_name = type_name
        self.user_rights = ()


class User:
    def __init__(self, username, email, password, user_type):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type

     
# class UserDatabase:
#     def __init__(self):
#         self.users = {}

#     def create_user(self, username, email, is_admin):
#         new_user = User(username, email, is_admin)
#         self.users.append(new_user)
#         print(f"User '{username}' created successfully!")

#     def display_users(self):
#         print("List of Users:")
#         for user in self.users:
#             print(f"Username: {user.username}, Email: {user.email}, Admin: {user.is_admin}")



def main():
    
    #user rights
    user_rights  = ("view cart Contents", "add items to carts", "remove items from cart", )
    admin_rights = ("add new product", "modify product", "delete produt", "add category", "modify category", "delete category")
    
    # User_types
    my_user  = User_type("user", user_rights) 
    my_admin = User_type("admin", admin_rights)

    # System Users    
    # users = {
    #             "user"  : User("u", "u1@g.com", "1", my_user),  #user
    #             "admin" : User("a","u2@g.com","1", my_admin)    #admin
    #         }
    
    users = {
                "user"  : "u",  #user
                "admin" : "a"    #admin
            }
    
    # database = UserDatabase()
    # admin_logged_in = False
    # user_logged_in = False # Need to add in logic for user login in while statment
    
    # username = 'g'
    # email = 'g'

    # database.create_user(username, email, is_admin=True)
    
    logged_in = False


    while True:
        if not logged_in:
            print("\n1. User Login\n2. Exit")
            choice = input("Enter your choice: ")
    
            if choice == '1':
                username = input("Enter username: ")
                # Assuming admin password validation here
                value = users.get(username)
                print(value)

                if username not in users:
                     print("Invalid username. Please try again.")
                else:
                    print("Welcome back, ", username,"!")
                    logged_in=True
                
                
            #     if username in users:
            #         logged_in = True
            #         print("Login successful!")
            #     else:
            #         print("Invalid username. Please try again.")
            elif choice == '2':
                 print("Exiting...")
                 break
            else:
                 print("Invalid choice. Please try again.")
        else:
             print("\nAdmin Options:")
             print("1. Create User\n2. Display Users\n3. Logout")
             admin_choice = input("Enter your choice: ")
    
    #         if admin_choice == '1':
    #             username = input("Enter username: ")
    #             email = input("Enter email: ")
    #             is_admin = input("Is the user an admin? (y/n): ").lower()
    #             if is_admin == 'y':
    #                 database.create_user(username, email, is_admin=True)
    #             else:
    #                 database.create_user(username, email)
    #         elif admin_choice == '2':
    #             database.display_users()
    #         elif admin_choice == '3':
    #             print("Admin logged out.")
    #             admin_logged_in = False
    #         else:
    #             print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
  
    
"""
Function to add
    1) Data validation for names, email addresses, etc.
    2) 
    
Useful Functions:
    variable = input('input something!: ')     #breaks the code for troubleshooting
    
    
"""