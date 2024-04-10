"""
Shopify App - Foundations: Programming Refresher Assignment

"""

class User_type:
    def __init__(self, type_name, rights):
        self.type_name = type_name
        self.rights = rights
        
        
    def display_rights(self, username):
        print("\nList of User Rights: ", self.rights)
        

class User:
    def __init__(self, username, email, password, user_type):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type
        
        
    def display_current_user(self):
        print("\nThe current user is: ",    self.username)
        print("The current email is: ",     self.email)
        print("The current password is: ",  self.password)
        print("The current user type is: ", self.user_type.type_name)
        print("The current user type rights are: ", self.user_type.rights)
        
      
class Category:
    def __init__(self, category_id):
        self.category_id = category_id
    
    
class Product:
    def __init__(self, product_id, product_name, category_id, price):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.price = price
        
        
class Catalog:
    product_list = {}
    
    def add_product(self, current_user, product_id, product_name, category_id, price):
        if 'Add New Product' in current_user.user_type.rights:
            #Logic to add product
            
            if product_id not in self.product_list:
                self.product_list[product_id] = Product(product_id, product_name, category_id, price)                    
            else:
                print("\nERROR: The product already exists")
        else:
            print("\nERROR: Current user has no permissions to add products")
            
                
    def remove_product(self, current_user, product_id):
        # print("\nDelete Existing Product Option Coming Soon!")
        if 'Delete Product' in current_user.user_type.rights:
            #Logic to delete product
            print("\nThis is where a product will get deleted.")
        else:
            print("\nERROR: Current user has no permissions to delete products") 
        
        
    def modifiy_product(self, current_user, product_id, product_name, category_id, price):
        if 'Modify Products' in current_user.user_type.rights:
            #Logic to modify product
            if product_id not in self.product_list:
                print("\nERROR: The product does not exist")
            else:
                self.product_list[product_id] = Product(product_id, product_name, category_id, price)
                print("\nProduct Modified!")
                print(self.product_list[product_id])
        else:
            print("\nERROR: current user has no permissions to add products")
            
            
    def display_product(self, current_user, my_catalog):
        if 'View Products' in current_user.user_type.rights:
            #Logic to display product
            
            print("\nProduct ID\tProduct Name\tCategory ID\tPrice\n")

            for product_id, value in my_catalog.product_list.items():
                print(f"{product_id}\t\t\t{value.product_name}\t\t\t{value.category_id}\t\t{value.price}")

        else:
            print("\nERROR: current user has no permissions to add products")

            
    def is_id_available(self, current_user, product_id):
        if 'View Products' in current_user.user_type.rights:
            #Logic to check if a product already exists in the catalog
            return product_id in self.product_list 
        else:
            print("\nERROR: Current user has no permissions to view products")


class Cart_product:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity
        
    def cart_product_total_price(self):
        print("temp")

class Cart:
    cart_list = {}
    
    def add_cartproduct(self, current_user, product_id, quantity, my_catalog):
        if 'Add Cart Product' in current_user.user_type.rights:
            #Logic to add product
            
            if product_id not in my_catalog.product_list:
                print("\nThis product does not exists. Please identify an existing product.")
            else:
                self.cart_list[product_id] = Cart_product(product_id, quantity)                    
        else:
            print("\nERROR: Current user has no permissions to add products")
            
            
    def remove_cartproduct(self, current_user, product_id, quantity, my_catalog):
        print("temp")
        
        
    def display_cart(self,current_user, my_cart, my_catalog):
        if 'View Cart' in current_user.user_type.rights:
            if not my_cart.cart_list:
                print("\nCart is empty.")
            else:                
                print("\nProduct Name\tCategory ID\tPrice\tQuantity\n")

                for product_id, value in my_cart.cart_list.items():
                    print(f"{my_catalog.product_list[product_id].product_name}\t\t\t{my_catalog.product_list[product_id].category_id}\t\t{my_catalog.product_list[product_id].price}\t\t{my_cart.cart_list[product_id].quantity}")
        else:
            print("\nERROR: current user has no permissions to add products")
            
            
    def cart_total_price(self):
        print("temp")
    
        
def display_users(users):
    print("\nList of Users:")
    for user in users:
        print(user)
        
        
def display_products(products):
    print("\nList of Products:")
    for product in products:
        print(product)
        
def repeat_choice_logic(current_user, my_catalog, my_cart, prompt_exiting,prompt_action, prompt_id, prompt_name, prompt_category, prompt_price, prompt_quantity, prompt_success, prompt_another, option):     ## could improve prompt by using a list and use array index for reference

    choice = 'y'
    
    while True: 
        
        if choice == 'n':
            print(prompt_exiting)               ## prompt_exiting = "\nExiting addition to cart..."
            break
        
        elif choice == 'x':
            print(prompt_exiting)
            break
            
        elif choice == 'y':
            
            print(prompt_action)                ## prompt_action = "\nLet's add some products to your cart:"
            
            while True:
                
                if choice =='n':
                    break
                
                product_id = input(prompt_id)   ## prompt_id = "\nEnter the product id: "
                
                if product_id == 'x':
                    break
                else:
                    
                    if option == 'Add Cart Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            quantity = input(prompt_quantity)       ## prompt_quantity = "\nHow many would you like to add to your cart: "
                            
                            my_cart.add_cartproduct(current_user, product_id, quantity, my_catalog)
                            
                            print(prompt_success)        ##prompt_success = "\nProduct added!"
                            
                            print(prompt_another)        ## prompt_another = "\nWould you like to add another product to the cart? y/n"
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                            
                    elif option == 'Add Catalog Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            print("A product with this ID already exists. Please enter a different ID.") 
                        else:                          
                            product_name    = input("\nEnter the product name: ")
                            category_id     = input("Enter the product category name: ") # This option must choose from existing list
                            price           = input("Enter the product price: ")
                    
                            my_catalog.add_product(current_user, product_id, product_name, category_id, price)
                    
                            print("\nProduct added!")
                            
                            print("\nWould you like to add another product to the catalog? y/n")
                            choice  = input("\nEnter your choice: ")
                            
                    elif option == 'Delete Catalog Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            
                            my_catalog.remove_product(current_user, product_id)
                            
                            print("\nProduct deleted!")
                            
                            print("\nWould you like to remove another product from the catalog? y/n")
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                                               
                        
                    else:
                        print("No option set for logic condition.")
                        
                
        else:
            print("Invalid choice. Please try again.")      ## this prompt can stay the same as it is used universally in all choice logic
        
        if product_id == 'x':
            print(prompt_exiting)
            break
        elif product_id == 'n':
            print(prompt_exiting)
            break


def main():
    
    #user rights
    user_rights  = ["View Products", "View Cart", "Add Cart Product", "Remove Cart Product"]
    admin_rights = ["Add New Product", "View Products", "Modify Products", "Delete Product", "Add Category", "Modify Category", "Delete Category", "Create User", "Display Users", "Delete User"]
    
    # User_types
    my_user  = User_type("user", user_rights) 
    my_admin = User_type("admin", admin_rights)
    
    # Add System Users    
    users = {
                "u"  : User("u", "u1@g.com", "1", my_user),  #user
                "a"  : User("a","u2@g.com","1", my_admin)    #admin
            }
    
    
    # Add System Products    
    my_catalog = Catalog()

    my_catalog.add_product(users['a'],"1", "Boots", "Shoes", 120)
    my_catalog.add_product(users['a'], "2", "Coats", "Clothes", 99)
    my_catalog.add_product(users['a'], "3", "Jackets", "Clothes", 150)
    my_catalog.add_product(users['a'], "4", "Caps", "Hats", 50)
    
    # Add System Cart
    my_cart = Cart()
    
    logged_in = False
    
    print("\n\nWelcome to the Demo Marketplace")

    while True:
        #Begin login: Logic to login the user and then provide options based on type
        if not logged_in:
            
            # If not already logged in, the system will request the user to login or exit
            
            print("\nMain Menu:\n1. User Login\n2. Exit")
            choice = input("\nEnter your choice: ")
    
            if choice == '1':
                for retry in range(5):
                    username = input("Enter username: ")
                    
                    #Check if username is defined in user dictionary - will need to update for password verification
                    if username not in users:
                        print("Invalid username. Please try again.")
                        retry += 1
                    else:
                        print("\nWelcome back, ",username,"!")
                        current_user = users[username]
                        logged_in = True
                        break
                else:
                    print("5 invalid choices made, returning to main menu.")
                    logged_in = False
                    
            elif choice == '2':
                 print("\nExiting...")
                 break
             
            else:
                 print("Invalid choice. Please try again.")
                 
        else:   #This else statement enters after a user logs in
        
            # This section of code is to understand how to get the current user type for option permissions
            #print(u_type)
            #User_type.display_rights(current_user)
            
            # Option menu appears based on user type of current login

            if current_user.user_type.type_name == 'user':
                
                print("\nUser Options:")
                print("1. View Cart Contents\n2. Add Items to Your Cart\n3. Remove Items from Your Cart\n4. View Product List\n5. View Product Category List\n6. Filter and View Product List by Category\n7. Checkout\n8. Logout")
                choice = input("\nEnter your choice: ")
            
                if choice == '1':       ## Display cart items 
                    # print("\nView Cart Contents Option Coming Soon!")
                    my_cart.display_cart(current_user, my_cart, my_catalog)
                elif choice == '2':    ## Add Items to Your Cart Option Coming Soon!")
                
                    prompt_exiting      = "\nExiting addition to cart..."
                    prompt_action       = "\nLet's add some products to your cart:"
                    prompt_id           = "\nEnter the product id: "
                    prompt_name         = ""
                    prompt_category     = ""
                    prompt_price        = ""
                    prompt_quantity     = "\nHow many would you like to add to your cart: "
                    prompt_success      = "\nProduct added!"
                    prompt_another      = "\nWould you like to add another product to the cart? y/n"
                    option              = "Add Cart Product"
                
                    repeat_choice_logic(current_user, my_catalog, my_cart, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_category, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                                                
                elif choice == '3':
                    print("\nRemove Items from Your Cart Option Coming Soon!")
                elif choice == '4':
                    # print("\nView Product List Option Coming Soon!")
                    my_catalog.display_product(current_user, my_catalog)
                elif choice == '5':
                    print("\nView Product Category List Option Coming Soon!")
                elif choice == '6':
                    print("\nFilter and View Product List by Category Option Coming Soon!")
                elif choice == '7':
                    print("\nCheckout Option Coming Soon!")
                elif choice == '8':
                    print("logged out.")
                    logged_in = False
                else:
                    print("Invalid choice. Please try again.")
            
            # Begin options once Admin login is achieved
            elif current_user.user_type.type_name == 'admin':
                            
                print("\nAdmin Options:")
                print("1.  View Product List\n2.  Add New Product\n3.  Modify Existing Product\n4.  Delete Existing Product\n5.  View Product Category List\n6.  Add New Product Category\n7.  Modify Existing Product Category\n8.  Delete Existing Product Category\n9.  View User List\n10. Add New User\n11. Modify Existing User\n12. Delete Existing User\n13. Logout")
                choice = input("\nEnter your choice: ")
        
                ## Improvement is to make a case statement?
                if   choice == '1':     ## Display Product List Option                 
                    my_catalog.display_product(current_user, my_catalog)
                    
                elif choice == '2':     ## Add New Product Option 
                
                    prompt_exiting      = "\nExiting new product addition..."
                    prompt_action       = "\nLet's add a new product:"
                    prompt_id           = "\nEnter the product id: "
                    prompt_name         = "\nEnter the product name: "
                    prompt_category     = "Enter the product category name: "
                    prompt_price        = "Enter the product price: "
                    prompt_quantity     = "\nHow many would you like to add to your cart: "
                    prompt_success      = "\nProduct added!"
                    prompt_another      = "\nWould you like to add another product to the cart? y/n"
                    option              = "Add Catalog Product"
                
                    repeat_choice_logic(current_user, my_catalog, my_cart, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_category, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                           
                    
                    # choice = 'y'
                    
                    # while True: 
                        
                    #     if choice == 'n':
                            
                    #         print("\nExiting new product addition...")
                    #         break
                        
                    #     elif choice == 'x':
                    #         print("\nLet's add a new product:")
                    #         break
                        
                    #     elif choice == 'y':
                            
                    #         print("\nLet's add a new product:")
                            
                    #         while True:
                                
                    #             if choice =='n':
                    #                 break
                                
                    #             product_id = input("\nEnter the product id: ")
                                
                    #             if product_id == 'x':
                    #                 break
                    #             else:
                    #                 if my_catalog.is_id_available(current_user, product_id):
                    #                     print("A product with this ID already exists. Please enter a different ID.") 
                    #                 else:                          
                    #                     product_name    = input("\nEnter the product name: ")
                    #                     category_id     = input("Enter the product category name: ") # This option must choose from existing list
                    #                     price           = input("Enter the product price: ")
                                
                    #                     my_catalog.add_product(current_user, product_id, product_name, category_id, price)
                                
                    #                     print("\nProduct added!")
                                        
                    #                     print("\nWould you like to add another product to the catalog? y/n")
                    #                     choice  = input("\nEnter your choice: ")
                                                        
                    #     else:
                    #         print("Invalid choice. Please try again.")
                        
                    #     if product_id == 'x':
                    #         print("\nExiting deletion from catalog...")
                    #         break
                    #     elif product_id == 'n':
                    #         print("\nExiting deletion from catalog...")
                    #         break
                    
                elif choice == '3':
                    print("\nModify Existing Product Option Coming Soon!")
                elif choice == '4':
                    # print("\nDelete Existing Product Option Coming Soon!")                                    
                    
                    prompt_exiting      = "\nExiting product removal..."
                    prompt_action       = "\nLet's delete a product:"
                    prompt_id           = "\nEnter the product id: "
                    prompt_name         = ""
                    prompt_category     = ""
                    prompt_price        = ""
                    prompt_quantity     = ""
                    prompt_success      = "\nProduct deleted!"
                    prompt_another      = "\nWould you like to remove another product from the catalog? y/n"
                    option              = "Delete Catalog Product"
                
                    repeat_choice_logic(current_user, my_catalog, my_cart, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_category, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                           
                    
                    # choice = 'y'
                    
                    # while True: 
                        
                    #     if choice == 'n':
                            
                    #         print("\nExiting product removal...")
                    #         break
                        
                    #     elif choice == 'x':
                    #         print("\nExiting deletion from catalog...")
                    #         break
                        
                    #     elif choice == 'y':
                            
                    #         print("\nLet's delete a product:")
                            
                    #         while True:
                                
                    #             if choice =='n':
                    #                 break
                                
                    #             product_id = input("\nEnter the product id: ")
                                
                    #             if product_id == 'x':
                    #                 break
                    #             else:
                    #                 if my_catalog.is_id_available(current_user, product_id):
                                        
                    #                     my_catalog.remove_product(current_user, product_id)
                                        
                    #                     print("\nProduct deleted!")
                                        
                    #                     print("\nWould you like to remove another product from the catalog? y/n")
                    #                     choice  = input("\nEnter your choice: ")
                    #                 else:
                    #                     print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                                                        
                    #     else:
                    #         print("Invalid choice. Please try again.")
                        
                    #     if product_id == 'x':
                    #         print("\nExiting deletion from catalog...")
                    #         break
                    #     elif product_id == 'n':
                    #         print("\nExiting deletion from catalog...")
                    #         break
                    
                elif choice == '5':
                    print("View Product Category List Option Coming Soon!")
                elif choice == '6':
                    print("\nAdd New Product Category Option Coming Soon!")
                elif choice == '7':
                    print("\nModify Existing Product Category Option Coming Soon!")
                elif choice == '8':
                    print("\nDelete Existing Product Category Option Coming Soon!")
                elif choice == '9':                    
                    display_users(users)
                elif choice == '10':                    
                    print("\nAdd New User Option Coming Soon!")
                elif choice == '11':
                    print("\nModify Existing User Option Coming Soon!")
                elif choice == '12':
                    print("\nDelete Existing User Option Coming Soon!")
                elif choice == '13':
                    print("logged out.")
                    logged_in = False
                else:
                    print("Invalid choice. Please try again.")
                    
            else:
                print("Error: Session user type should always have an assignment!")
                break

    print("\nThank You for Visiting the Demo Marketplace")

if __name__ == "__main__":
    main()
    
  
    
"""
Function to add
    - Data validation for names, email addresses, etc.
    - Need to add rights based on user type
    - Update usernames to include password verification
    - Modularize for more efficient code
    - Category_ID in adding product must choose from existing list
    - Change the 'list' currently defined for user permissions to a set (that is not a truple)
    - Define a new class for switch statements that includes methods for user and admin option menus
    - When a user logs out, it clears the cart
    - Eliminate redundancy logic to check if product ID exists in main() and user 'Add Cart Product' / admin 'Add product' options
    - Finish 'repeat_choice_logic' method that will contain the repetitive logic for user decision for repeating add/remove/modify logic
        - Reduce logic code lines by implementing OR statements and other logic improvements
        - Update 'add_new_product' admin option logic to follow the new 'repeat_choice_logic' as it is outdated
    
Useful Functions:
    rando = input('input something!: ')     #breaks the code for troubleshooting
    
    
"""