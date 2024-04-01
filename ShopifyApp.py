"""
Shopify App - Foundations: Programming Refresher Assignment

"""

class User_type:
    def __init__(self, type_name, user_rights):
        self.type_name = type_name
        self.user_rights = ()
        
    def display_rights(self, username):
        print("\nList of User Rights: ", self.user_rights)
        

class User:
    def __init__(self, username, email, password, user_type):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type
        
    def display_current_user(self):
        print("\nThe current user is: ",    self.username)
        #print("The current email is: ",     self.email)
        #print("The current password is: ",  self.password)
        #print("The current user type is: ", self.user_type)
        
        
class Product:
    def __init__(self, product_id, product_name, category_id, price):
        self.product_id = product_id
        self.product_name = product_name
        self.cateogry_id = category_id
        self.price = price
     
        
def display_users(users):
    print("\nList of Users:")
    for user in users:
        print(user)
        
def display_products(products):
    print("\nList of Products:")
    for product in products:
        print(product)


def main():
    
    logged_in = False
    
    #user rights
    user_rights  = ("view cart contents", "add items to cart", "remove items from cart", )
    admin_rights = ("add new product", "modify product", "delete produt", "add category", "modify category", "delete category", "create user", "display users", "delete user")
    
    
    # User_types
    my_user  = User_type("user", user_rights) 
    my_admin = User_type("admin", admin_rights)
    

    # System Users    
    users = {
                "u"  : User("u", "u1@g.com", "1", my_user),  #user
                "a" : User("a","u2@g.com","1", my_admin)    #admin
            }
    
    # System Products    
    products = {
                "Boots"   : Product("1", "Shoes", "1", 120),
                "Coats"   : Product("2", "Clothes", "2", 99),
                "Jackets" : Product("3", "Clothes", "2", 150),
                "Caps"    : Product("4", "Hats", "2", 50),
               }
    
    print("\n\nWelcome to the Demo Marketplace")

    while True:
        #Begin login: Logic to login the user and then provide options based on type
        if not logged_in:
            
            # If not already logged in, the system will request the user to login or exit
            print("\n1. User Login\n2. Exit")
            choice = input("\nEnter your choice: ")
    
            if choice == '1':
                for retry in range(5):
                    username = input("Enter username: ")
                    
                    #Check if username is defined in user dictionary - will need to update for password verification
                    if username not in users:
                        print("Invalid username. Please try again.")
                        retry += 1
                    else:
                        print("Welcome back, ",username,"!")
                        current_user = users['u']
                        current_type = 'admin'  ## 1) I would like to set the current user type here based on user or admin. 2) I would like to add an option for the admin to choose between admin or user view
                        logged_in = True
                        break
                else:
                    print("you keep making invalid choices, exiting.")
                    logged_in = False
                    
            elif choice == '2':
                 print("\nExiting...")
                 break
             
            else:
                 print("Invalid choice. Please try again.")
                 
        else:   #This else statement enters after a user logs in
        
            # This section of code is to understand how to get the current user type for option permissions
            User.display_current_user(current_user)
            #print(u_type)
            #User_type.display_rights(current_user)
            
            # Begin options once Admin login is achieved
            if current_type == 'user':
                
                print("\nUser Options:")
                print("1. View Cart Contents\n2. Add Items to Your Cart\n3. Remove Items from Your Cart\n4. View Product List\n5. View Product Category List\n6. Filter and View Product List by Category\n7. Checkout")
                user_choice = input("\nEnter your choice: ")
            
                if user_choice == '1':     ## 
                    print("\nView Cart Contents Option Coming Soon!")
                elif user_choice == '2':
                    print("\nAdd Items to Your Cart Option Coming Soon!")
                elif user_choice == '3':
                    print("\nRemove Items from Your Cart Option Coming Soon!")
                elif user_choice == '4':
                    print("\nView Product List Option Coming Soon!")
                elif user_choice == '5':
                    print("\nView Product Category List Option Coming Soon!")
                elif user_choice == '6':
                    print("\nFilter and View Product List by Category Option Coming Soon!")
                elif user_choice == '7':
                    print("\nCheckout Option Coming Soon!")
            
            # Begin options once Admin login is achieved
            elif current_type == 'admin':
                            
                print("\nAdmin Options:")
                print("1.  View Product List\n2.  Add New Product\n3.  Modify Existing Product\n4.  Delete Existing Product\n5.  View Product Category List\n6.  Add New Product Category\n7.  Modify Existing Product Category\n8.  Delete Existing Product Category\n9.  View User List\n10. Add New User\n11. Modify Existing User\n12. Delete Existing User\n13. Logout")
                admin_choice = input("\nEnter your choice: ")
        
                ## Improvement is to make a case statement?
                if   admin_choice == '1':     ## Add New Product Option
                    print("\nView Product List Option Coming Soon!")                   
                    display_products(products)
                elif admin_choice == '2':
                    print("\nAdd New Product Option Coming Soon!")
                    
                    ## Request info for new products based on needs below:
                    newprod_id    = input("\nEnter the product name: ") #This option should be the next iteration in the list, IDs are autodetermined
                    newprod_name  = input("\nEnter the product name: ")
                    newprod_cat   = input("\nEnter the product category name: ") # This option must choose from existing list
                    newprod_price = input("\nEnter the product price: ")
                    
                elif admin_choice == '3':
                    print("\nModify Existing Product Option Coming Soon!")
                elif admin_choice == '4':
                    print("\nDelete Existing Product Option Coming Soon!")
                elif admin_choice == '5':
                    print("View Product Category List Option Coming Soon!")
                elif admin_choice == '6':
                    print("\nAdd New Product Category Option Coming Soon!")
                elif admin_choice == '7':
                    print("\nModify Existing Product Category Option Coming Soon!")
                elif admin_choice == '8':
                    print("\nDelete Existing Product Category Option Coming Soon!")
                elif admin_choice == '9':                    
                    display_users(users)
                elif admin_choice == '10':                    
                    print("\nAdd New User Option Coming Soon!")
                elif admin_choice == '11':
                    print("\nModify Existing User Option Coming Soon!")
                elif admin_choice == '12':
                    print("\nDelete Existing User Option Coming Soon!")
                elif admin_choice == '13':
                    print("logged out.")
                    logged_in = False
                else:
                    print("Invalid choice. Please try again.")
                    
            else:
                print("Error: Seesion user type should always have an assignment!")

    print("\nThank You for Visiting the Demo Marketplace")

if __name__ == "__main__":
    main()
    
  
    
"""
Function to add
    1) Data validation for names, email addresses, etc.
    2) Need to add rights based on user type
    3) Update usernames to include password verification
    4) Modularize for more efficient code
    
Useful Functions:
    rando = input('input something!: ')     #breaks the code for troubleshooting
    
    
"""