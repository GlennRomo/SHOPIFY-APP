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
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        
        
class Category_catalog:
    category_list = {}
    
    def add_category(self, current_user, category_id, category_name):
        if 'Add Category' in current_user.user_type.rights:
            #Logic to add category
            
            if category_id not in self.category_list:
                self.category_list[category_id] = Category(category_id, category_name)                    
            else:
                print("\nERROR: The category already exists")
        else:
            print("\nERROR: Current user has no permissions to add categories")
            
            
    def modify_category(self, current_user, category_id, category_name, my_categories):
        if 'Modify Products' in current_user.user_type.rights:
            #Logic to modify product
            if category_id not in self.category_list:
                print("\nERROR: The category does not exist")
            else:
                self.category_list[category_id] = Category(category_id, category_name)
        else:
            print("\nERROR: current user has no permissions to modify products")
            
            
    def display_categories(self, current_user, my_categories):
        if 'View Categories' in current_user.user_type.rights:
            #Logic to display product
            
            print("\nCategory ID\tCategory Name")

            for category_id, value in my_categories.category_list.items():
                print(f"{category_id}\t\t\t{value.category_name}")

        else:
            print("\nERROR: current user has no permissions to view categories")
            
    def remove_category(self, users, session_manager, current_user, category_id):
        if 'Delete Category' in current_user.user_type.rights:
            #Logic to delete product
            if category_id not in self.category_list:
                print("\nThis category does not exist. Please identify an existing category.")
            else:
                input("Press enter to continue...")
                
                for user, user_value in users.items():
                    print(user, users[user].user_type.type_name)
                    input("Press enter to continue0...")
                    if users[user].user_type.type_name == 'user':
                        cart_list_copy = session_manager.session_list[users[user]].cart_list.copy()
                        for product_id, cart_value in cart_list_copy.items():
                            print(product_id, cart_value.category, self.category_list[category_id].category_name)
                            input("Press enter to continue1...")
                            if cart_value.category == self.category_list[category_id].category_name:
                                input("Press enter to continue2...")
                                del session_manager.session_list[users[user]].cart_list[product_id]
                            
                            
                del self.category_list[category_id]
                        
                    
                
        else:
            print("\nERROR: Current user has no permissions to delete products") 
            
            
    def is_id_available(self, current_user, category_id):
        if 'View Products' in current_user.user_type.rights:
            #Logic to check if a product already exists in the catalog
            return category_id in self.category_list 
        else:
            print("\nERROR: Current user has no permissions to check products")

    
class Product:
    def __init__(self, product_id, product_name, category_id, price, my_categories):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id =  my_categories.category_list[category_id].category_id
        self.category_name = my_categories.category_list[category_id].category_name
        self.price = price
        
        
class Catalog:
    product_list = {}
    
    def add_product(self, current_user, product_id, product_name, category_id, price, my_categories):
        if 'Add New Product' in current_user.user_type.rights:
            #Logic to add product
            
            if product_id not in self.product_list:
                if category_id not in my_categories.category_list:
                    print("\nERROR: That category does not exist. Please enter a valid category id.")
                else:
                    self.product_list[product_id] = Product(product_id, product_name, category_id, price, my_categories)                    
            else:
                print("\nERROR: The product already exists")
        else:
            print("\nERROR: Current user has no permissions to add products")
            
                
    def remove_product(self, current_user, product_id):
        if 'Delete Product' in current_user.user_type.rights:
            #Logic to delete product
            if product_id not in self.product_list:
                print("\nThis product does not exist. Please identify an existing product.")
            else:
                del self.product_list[product_id]
        else:
            print("\nERROR: Current user has no permissions to delete products") 
        
        
    def modify_product(self, current_user, product_id, product_name, category_id, price, my_categories):
        if 'Modify Products' in current_user.user_type.rights:
            #Logic to modify product
            if product_id not in self.product_list:
                print("\nERROR: The product does not exist")
            else:
                self.product_list[product_id] = Product(product_id, product_name, category_id, price, my_categories)
        else:
            print("\nERROR: current user has no permissions to modify products")
            
            
    def display_product(self, current_user, my_catalog):
        if 'View Products' in current_user.user_type.rights:
            #Logic to display product
            
            print("\nProduct ID\tProduct Name\tCategory Name\tPrice\n")

            for product_id, value in my_catalog.product_list.items():
                print(f"{product_id}\t\t\t{value.product_name}\t\t\t{value.category_name}\t\t{value.price}")

        else:
            print("\nERROR: current user has no permissions to view products")

            
    def is_id_available(self, current_user, product_id):
        if 'View Products' in current_user.user_type.rights:
            #Logic to check if a product already exists in the catalog
            return product_id in self.product_list 
        else:
            print("\nERROR: Current user has no permissions to check products")


class Cart_product:
    def __init__(self, product_id, quantity, my_catalog, my_categories):
        self.product_id = product_id
        self.quantity   = quantity
        self.category   = my_categories.category_list[product_id].category_name
        self.price      = my_catalog.product_list[product_id].price
        
    def total_price(self):
        return self.quantity * self.price

class Cart:
    def __init__(self):
        self.cart_list = dict()
    
    def add_cartproduct(self, current_user, product_id, quantity, my_catalog, my_categories, session_manager):
        if 'Add Cart Product' in current_user.user_type.rights:
            #Logic to add product
            
            if product_id not in my_catalog.product_list:
                print("\nThis product does not exists. Please identify an existing product.")
            else:
                quantity = int(quantity)  ## Build in error if input is not a number
                self.cart_list[product_id] = Cart_product(product_id, quantity, my_catalog, my_categories)                    
        else:
            print("\nERROR: Current user has no permissions to add products")
            
            
    def remove_cartproduct(self, current_user, next_choice, product_id, quantity, my_catalog, my_categories):
        if 'Remove Cart Product' in current_user.user_type.rights:
            #Logic to remove product
            
            if product_id not in my_catalog.product_list:
                print("\nThis product does not exist. Please identify an existing product.")
            else:
                if next_choice == '2':
                    if self.cart_list[product_id].quantity >= quantity and self.cart_list[product_id].quantity > 0:
                        new_quantity = self.cart_list[product_id].quantity - quantity
                        self.cart_list[product_id] = Cart_product(product_id, new_quantity, my_catalog, my_categories)
                    else:
                        print("You must select a number of products that are less than the amount of that item in the cart and a number higher than zero.")
                elif next_choice == '1':
                    del self.cart_list[product_id]
        else:
            print("\nERROR: Current user has no permissions to remove cart products")
        
        
    def display_cart(self,current_user, session_manager, my_catalog):
        if 'View Cart' in current_user.user_type.rights:
            if not session_manager.session_list[current_user].cart_list:
                print("\nCart is empty.")
            else:                
                print("\nProduct ID\tProduct Name\tCategory ID\tPrice\tQuantity")
                
                for product_id, value in session_manager.session_list[current_user].cart_list.items():
                    print(f"{my_catalog.product_list[product_id].product_id}\t\t\t{my_catalog.product_list[product_id].product_name}\t\t\t{my_catalog.product_list[product_id].category_id}\t\t\t{my_catalog.product_list[product_id].price}\t\t{session_manager.session_list[current_user].cart_list[product_id].quantity}")
        else:
            print("\nERROR: current user has no permissions to add products")
            
            
    def cart_total_price(self, current_user):
        if 'Checkout' in current_user.user_type.rights:
            if not self.cart_list:
                print("\nCart is empty.")
            else:                
                total = 0
                for product_id, item in self.cart_list.items():
                    total += item.total_price()

        else:
            print("\nERROR: current user has no permissions to add products")
            
        return total
 
 
# class Session:
#     def __init__(self, current_user, session_id):
#         self.session_cart = Cart()
#         self.current_user = current_user
#         self.session_id = session_id

    
class SessionManager:
    def __init__(self):
        self.session_list = {}

    def create_session(self, current_user):
        self.session_list[current_user] = Cart()

    def get_session_cart(self, current_user):
        return self.session_list.get(current_user)
    
    def get_user_sessions(self, current_user):
        user_session_ids = []
        for session_id, session in self.session_list.items():
            if self.session_list[current_user].current_user == current_user:
                user_session_ids.append(session_id)
        return user_session_ids
    
    def has_sessions_for_user(self, current_user):
        for session in self.session_list.values():
            if session['user'] == current_user:
                return True
        return False
    
    
class Payment:      ## How do I initialize this function without defining a system variable (the output kept saying "payment_logic() missing 1 required positional argument: 'total_price'")
    
    # def __init__(self, current_user, total_price):
    #     self.current_user   = current_user
    #     self.total_price    = total_price
    
    def payment_choice_logic(self, current_user, session_manager):
        
        tax_percentage = 0.12
        
        cart_price = session_manager.session_list[current_user].cart_total_price(current_user)
        tax_price = cart_price * tax_percentage
        total_price = cart_price + tax_price
        
        print("\nYour total price is: \t$ {:.2f}".format(cart_price))
        print("Your total tax is: \t\t$ {:.2f}".format(tax_price))
        print("Your total price is: \t$ {:.2f}".format(total_price))
        
        while True:
        
            print("\nPlease choose the payment option:\n1. Net Banking\n2. PayPal\n3. Credit/Debit Card\n4. Google Pay\n5. Apple Pay\n6. Unified Payment Interface")
            pay_option = input("\nPlease enter your choice: ")
            
            if pay_option == '1':
                print("\n\nRedirecting to the portal for Net Banking to make a payment of ${:.2f}".format(total_price))
                print("\nYour order is successfully placed!!")
                session_manager.session_list[current_user].cart_list.clear()
                break
            
            elif pay_option == '2':
                print("\n\nRedirecting to the portal for PayPal to make a payment of ${:.2f}".format(total_price))
                print("\nYour order is successfully placed!!")
                session_manager.session_list[current_user].cart_list.clear()
                break
                
            elif pay_option == '3':
                print("\n\nRedirecting to the portal for Credit/Debit Cards to make a payment of ${:.2f}".format(total_price))
                print("\nYour order is successfully placed!!")
                session_manager.session_list[current_user].cart_list.clear()
                break
                
            elif pay_option == '4':
                print("\n\nRedirecting to the portal for Google Pay to make a payment of ${:.2f}".format(total_price))
                print("\nYour order is successfully placed!!")
                session_manager.session_list[current_user].cart_list.clear()
                break
                
            elif pay_option == '5':
                print("\n\nRedirecting to the portal for Apple Pay to make a payment of ${:.2f}".format(total_price))
                print("\nYour order is successfully placed!!")
                session_manager.session_list[current_user].cart_list.clear()
                break
                
            elif pay_option == '6':
                print("\n\nRedirecting to the portal for Unified Payment Interface to make a payment of ${:.2f}".format(total_price))
                print("\nYour order is successfully placed!!")
                session_manager.session_list[current_user].cart_list.clear()
                break
                
            elif pay_option == 'x':
                break
            
            else:
                print("\nThat catalog ID already exists in the catalog. Please enter a valid catalog ID. Enter x to exit.")
    
        
def display_users(users):
    print("\nList of Users:")
    for user in users:
        print(user)
        
        
def display_products(products):
    print("\nList of Products:")
    for product in products:
        print(product)
        
        
        
def repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting,prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option):     ## could improve prompt by using a list and use array index for reference

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
                            
                            session_manager.session_list[current_user].add_cartproduct(current_user, product_id, quantity, my_catalog, my_categories, session_manager)
                            
                            print(prompt_success)        ##prompt_success = "\nProduct added!"
                            
                            print(prompt_another)        ## prompt_another = "\nWould you like to add another product to the cart? y/n"
                            choice  = input("\nEnter your choice: ")    ## This should never have a value other than n, x, or y; passed through wwith 4
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                            
                    elif option == 'Delete Cart Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            if product_id not in session_manager.session_list[current_user].cart_list:
                                print("\nThis product is not in your cart.")
                            else:
                                while True:
                                    next_choice = input(prompt_name)
                                    
                                    if next_choice == '1' or next_choice == '2':
                                        
                                        quantity = 0
                                        
                                        if next_choice == '2':
                                            quantity = input(prompt_quantity)                            
                                            quantity = int(quantity)
                                            
                                        session_manager.session_list[current_user].remove_cartproduct(current_user, next_choice, product_id, quantity, my_catalog, my_categories)
                                        
                                        print(prompt_success)
                                            
                                        break
                                    else:
                                        # Input is not valid, prompt the user to try again
                                        print("Invalid input. Please enter either 1 or 2. Enter x to exit.")
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                            
                    elif option == 'Add Catalog Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            print("A product with this ID already exists. Please enter a different ID. Enter x to exit.") 
                        else:       
                            
                            product_name    = input(prompt_name)
                            price           = input(prompt_price)
                            
                            while True:
                                category_id     = input(prompt_categoryID) # This option must choose from existing list
                                
                                if my_categories.is_id_available(current_user, category_id):
                                    my_catalog.add_product(current_user, product_id, product_name, category_id, price, my_categories)
                                    print(prompt_success)
                                    break
                                else:
                                    # Input is not valid, prompt the user to try again
                                    print("Invalid category id. Please enter a valid category id. Enter x to exit.")
                                    
                                if category_id == 'x':
                                    print("Cancelling new product addition...")
                                    break
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")
                            
                    elif option == 'Delete Catalog Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            
                            my_catalog.remove_product(current_user, product_id)
                            
                            print(prompt_success)
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                                    
                    elif option == 'Modify Catalog Product':
                        if my_catalog.is_id_available(current_user, product_id):
                            
                            product_name    = input(prompt_name)
                            category_id     = input(prompt_categoryID) # This option must choose from existing list
                            price           = input(prompt_price)
                            
                            my_catalog.modify_product(current_user, product_id, product_name, category_id, price, my_categories)
                            
                            print(prompt_success)
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")                          
                            
                    elif option == 'Add Category':
                        if my_categories.is_id_available(current_user, product_id):
                            print("\nThat catalog ID already exists in the catalog. Please enter a valid catalog ID. Enter x to exit.")
                            
                        else:
                            category_id     = product_id
                            category_name   = input(prompt_categoryname)
                            
                            my_categories.add_category(current_user, category_id, category_name)
                            
                            print(prompt_success)
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")                            
                            
                    elif option == 'Modify Category':
                        if my_categories.is_id_available(current_user, product_id):
                            
                            my_categories.display_categories(current_user, my_categories)
                            
                            category_id = product_id
                            print("\n")
                            category_name   = input(prompt_name)
                            
                            my_categories.modify_category(current_user, category_id, category_name, my_categories)
                            
                            print(prompt_success)
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat category ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")  
                            
                    elif option == 'Delete Category':
                            
                        category_id     = product_id
                        
                        if my_categories.is_id_available(current_user, category_id):
                            
                            my_categories.remove_category(users, session_manager, current_user, category_id)
                            
                            print(prompt_success)
                            
                            print(prompt_another)
                            choice  = input("\nEnter your choice: ")
                        else:
                            print("\nThat product ID does not exist in the catalog. Please enter a valid product ID. Enter x to exit.")
                            
                    else:
                        print("No option set for logic condition.")
                        

                        
        else:
            print("Invalid choice. Please try again.")
        
        if product_id == 'x' or product_id == 'n':
            print(prompt_exiting)
            break






def main():
    
    while True:
    
        try:          
            
            first_pass = 0
            
            if first_pass == 0:
        
                #user rights
                user_rights  = ["View Products", "View Cart", "Add Cart Product", "Remove Cart Product", "View Categories", "Checkout", "Create Session", "Change Session"]
                admin_rights = ["Add New Product", "View Products", "Modify Products", "Delete Product", "Add Category", "Delete Category", "View Categories", "Modify Category", "Delete Category", "Create User", "Display Users", "Delete User"]
                
                # User_types
                my_user  = User_type("user", user_rights) 
                my_admin = User_type("admin", admin_rights)
                
                # Add System Users    
                users = {
                            "guest" : User("guest", "", "", my_user),       #guest     
                            "u1"    : User("u1", "u1@g.com", "1", my_user), #user 1
                            "u2"    : User("u2", "u2@g.com", "2", my_user), #user 2
                            "a"     : User("a","u2@g.com","3", my_admin)    #admin
                        }
                
                
                
                # Add System Session Manager
                session_manager = SessionManager()
                session_manager.create_session(users['u1'])
                session_manager.create_session(users['u2'])
                session_manager.create_session(users['guest'])
                
                # Add System Category
                my_categories = Category_catalog()
                
                my_categories.add_category(users['a'], "1", "Footwear")
                my_categories.add_category(users['a'], "2", "Upperwear")
                my_categories.add_category(users['a'], "3", "Lowerwear")
                my_categories.add_category(users['a'], "4", "Hats")
                my_categories.add_category(users['a'], "5", "Electronics")
                my_categories.add_category(users['a'], "6", "Appliances")
                my_categories.add_category(users['a'], "7", "Food")
                
                # Add System Products    
                my_catalog = Catalog()
            
                my_catalog.add_product(users['a'],"1", "Boots", "1", 120, my_categories)
                my_catalog.add_product(users['a'], "2", "Coats", "2", 99, my_categories)
                my_catalog.add_product(users['a'], "3", "Jackets", "2", 150, my_categories)
                my_catalog.add_product(users['a'], "4", "Caps", "4", 50, my_categories)
                my_catalog.add_product(users['a'], "5", "Washer", "6", 250, my_categories)
                my_catalog.add_product(users['a'], "6", "Laptop", "5", 50, my_categories)
                my_catalog.add_product(users['a'], "7", "Bread", "7", 50, my_categories)
                
                # Add System Payment
                payment_object = Payment()
                
                first_pass+=1
            
            logged_in = False
            
            print("\n\nWelcome to the Demo Marketplace")
        
            while True:
            
                #Begin login: Logic to login the user and then provide options based on type
                if not logged_in:
                    
                    # If not already logged in, the system will request the user to login or exit
                    
                    print("\nMain Menu:\n1. Login\n2. Exit")
                    choice = input("\nEnter your choice: ")
            
                    if choice == '1':
                        for retry in range(5):
                            username = input("Enter username: ")
                            
                            #Check if username is defined in user dictionary - will need to update for password verification
                            if username == 'guest':
                                print("\nWelcome, ",username,"!")
                                current_user = users[username]
                                logged_in = True
                                break
                            elif username not in users:
                                print("Invalid username. Please try again.")
                                retry += 1
                            else:
                                password = input("Enter password: ")
                                
                                if password == users[username].password:
                                    print("\nWelcome back, ",username,"!")
                                    current_user = users[username]
                                    logged_in = True
                                    break
                                else:
                                    print("\nIncorrect Password. Please try again...")
                        else:
                            print("5 invalid choices made, returning to main menu.")
                            logged_in = False
                            
                    elif choice == '2':
                         print("\nExiting...")
                         break
                     
                    else:
                         print("Invalid choice. Please try again.")
                         
                else:   #This else statement enters after a user logs in
                
                    # This section shows menu options based on current user type
        
                    if current_user.user_type.type_name == 'user':
                   
                        print("\nUser Options:")
                        print("1.  View Cart Contents\n2.  Add Items to Your Cart\n3.  Remove Items frm Your Cart\n4.  View Product List\n5.  View Category List\n6. Filter and View Product List by Category\n7. Checkout\n8. Logout")
                        choice = input("\nEnter your choice: ")
                    
                        if choice == '1':    ## View Cart Contents Option
                            session_manager.session_list[current_user].display_cart(current_user, session_manager, my_catalog)
                            
                        elif choice == '2':    ## Add Items to Your Cart Option
                        
                            prompt_exiting      = "\nExiting addition to cart..."
                            prompt_action       = "\nLet's add some products to your cart:"
                            prompt_id           = "\nEnter the product id: "
                            prompt_name         = ""
                            prompt_categoryID   = ""
                            prompt_categoryname = ""
                            prompt_price        = ""
                            prompt_quantity     = "\nHow many would you like to add to your cart: "
                            prompt_success      = "\nProduct added!"
                            prompt_another      = "\nWould you like to add another product to the cart? y/n"
                            option              = "Add Cart Product"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                                                        
                        elif choice == '3':    ## Remove Items from Your Cart Option
                            
                            prompt_exiting      = "\nExiting removal from cart..."
                            prompt_action       = "\nLet's delete some products from your cart:"
                            prompt_id           = "\nEnter the product id: "
                            prompt_name         = "\nWould you like to remove all items with this product id or just some?\n[1 - 'remove all'  2 - 'remove some']\nEnter your choice:  "
                            prompt_categoryID   = ""
                            prompt_categoryname = ""
                            prompt_price        = ""
                            prompt_quantity     = "\nHow many would you like to remove: "
                            prompt_success      = "\nProduct(s) deleted!"
                            prompt_another      = "\nWould you like to remove another product from your cart? y/n"
                            option              = "Delete Cart Product"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
        
                        elif choice == '4':    ## View Product Option 
                            my_catalog.display_product(current_user, my_catalog)
                            
                        elif choice == '5':    ## View Category List
                            my_categories.display_categories(current_user, my_categories)
                            
                        elif choice == '6':
                            print("\nFilter and View Product List by Category Option Coming Soon!")
                            
                        elif choice == '7':     ## Checkout Option
                            payment_object.payment_choice_logic(current_user, session_manager)
                                
                        elif choice == '8':
                                                        
                            if current_user == users['guest']:
                                if session_manager.session_list[current_user].cart_list:
                                    confirm = input("This will erase your cart. Are you sure you want to log out? (y/n) ")
                                    if confirm == 'y':
                                        session_manager.session_list[current_user].cart_list.clear()
                                        print("\nLogged out.")
                                        logged_in = False
                                else:
                                    print("\nLogged out.")
                                    logged_in = False
                            else:
                                print("\nLogged out.")
                                logged_in = False
                            
                        else:
                            print("Invalid choice. Please try again.")
                            
                    
                    # Begin options once Admin login is achieved
                    elif current_user.user_type.type_name == 'admin':
                                    
                        print("\nAdmin Options:")
                        print("1.  View Product List\n2.  Add New Product\n3.  Modify Existing Product\n4.  Delete Existing Product\n5.  View Category List\n6.  Add New Category\n7.  Modify Existing Category\n8.  Delete Existing Category\n9.  View User List\n10. Add New User\n11. Modify Existing User\n12. Delete Existing User\n13. Logout")
                        choice = input("\nEnter your choice: ")
                
                        ## Improvement is to make a case statement?
                        if   choice == '1':     ## Display Product List Option   
                        
                            my_catalog.display_product(current_user, my_catalog)
                            
                        elif choice == '2':     ## Add New Product Option 
                        
                            prompt_exiting      = "\nExiting new product addition..."
                            prompt_action       = "\nLet's add a new product:"
                            prompt_id           = "\nEnter the product id: "
                            prompt_name         = "\nEnter the product name: "
                            prompt_categoryID   = "Enter the product category id: "
                            prompt_categoryname = ""
                            prompt_price        = "Enter the product price: "
                            prompt_quantity     = "\nHow many would you like to add to your cart: "
                            prompt_success      = "\nProduct added!"
                            prompt_another      = "\nWould you like to add another product to the cart? y/n"
                            option              = "Add Catalog Product"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                                   
                            
                        elif choice == '3':     ## Modify Existing Product Option
                            
                            prompt_exiting      = "\nExiting product modification..."
                            prompt_action       = "\nLet's modify a product:"
                            prompt_id           = "\nEnter the product id: "
                            prompt_name         = "\nWhat would you like to change the name to? "
                            prompt_categoryID   = "\nWhich category would you like to assign this product to?"
                            prompt_categoryname = ""
                            prompt_price        = "\nWhat would you like to change the price to?"
                            prompt_quantity     = ""
                            prompt_success      = "\nProduct modified!"
                            prompt_another      = "\nWould you like to modify another product from the catalog? y/n"
                            option              = "Modify Catalog Product"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
        
                            
                        elif choice == '4':     ## Delete Existing Product Option                                 
                            
                            prompt_exiting      = "\nExiting product removal..."
                            prompt_action       = "\nLet's delete a product:"
                            prompt_id           = "\nEnter the product id: "
                            prompt_name         = ""
                            prompt_categoryID   = ""
                            prompt_categoryname = ""
                            prompt_price        = ""
                            prompt_quantity     = ""
                            prompt_success      = "\nProduct deleted!"
                            prompt_another      = "\nWould you like to remove another product from the catalog? y/n"
                            option              = "Delete Catalog Product"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
        
                            
                        elif choice == '5':     ## View Category Catalog Option
                        
                            my_categories.display_categories(current_user, my_categories)
                            
                        elif choice == '6':     ## New Category Option
                            
                            prompt_exiting      = "\nExiting new category addition..."
                            prompt_action       = "\nLet's add a new category:"
                            prompt_id           = "\nEnter the new category id: "
                            prompt_name         = ""
                            prompt_categoryID   = "\nEnter the new category id: "
                            prompt_categoryname = "\nEnter the new category name: "
                            prompt_price        = ""
                            prompt_quantity     = ""
                            prompt_success      = "\nCategory added!"
                            prompt_another      = "\nWould you like to add another category to the catalog? y/n"
                            option              = "Add Category"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                            
                            
                        elif choice == '7':     ## Modify Existing Category Option
                            
                            prompt_exiting      = "\nExiting category modification..."
                            prompt_action       = "\nLet's modify a category:"
                            prompt_id           = "\nEnter the category id you would like to modify: "
                            prompt_name         = "What would you like to change the category name to: "
                            prompt_categoryID   = ""
                            prompt_categoryname = ""
                            prompt_price        = ""
                            prompt_quantity     = ""
                            prompt_success      = "\nCategory modified!"
                            prompt_another      = "\nWould you like to modify another category in the catalog? y/n"
                            option              = "Modify Category"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                            
                            
                        elif choice == '8':     ## Delete Category Option
                            
                            prompt_exiting      = "\nExiting category deletion..."
                            prompt_action       = "\nLet's delete a category:"
                            prompt_id           = "\nEnter the category id you would like to remove: "
                            prompt_name         = ""
                            prompt_categoryID   = ""
                            prompt_categoryname = ""
                            prompt_price        = ""
                            prompt_quantity     = ""
                            prompt_success      = "\nCategory deleted!"
                            prompt_another      = "\nWould you like to delete another category in the catalog? y/n"
                            option              = "Delete Category"
                        
                            repeat_choice_logic(users, current_user, my_catalog, session_manager, my_categories, prompt_exiting, prompt_action, prompt_id, prompt_name, prompt_categoryID, prompt_categoryname, prompt_price, prompt_quantity, prompt_success, prompt_another, option)
                            
                            
                        elif choice == '9':     ## View User List Option         
                            display_users(users)
                            
                        elif choice == '10':                    
                            print("\nAdd New User Option Coming Soon!")
                            
                        elif choice == '11':
                            print("\nModify Existing User Option Coming Soon!")
                            
                        elif choice == '12':
                            print("\nDelete Existing User Option Coming Soon!")
                            
                        elif choice == '13':    ## Logout Option
                            print("logged out.")
                            logged_in = False
                            
                        else:
                            print("Invalid choice. Please try again.")
                            
                    else:
                        print("Error: Session user type should always have an assignment!")
                        break
        
            print("\nThank You for Visiting the Demo Marketplace")
            break
        
        
        
        
        except Exception:   ## as e:
            
            # print("\n\n\nAn error occurred:", e)
            print("")
        
        
        
        
        

if __name__ == "__main__":
    main()
    
  
    
"""
Functionality to add
    - Add Cart Product
        - Option ''Add Cart Product'' in repeat_choice_logic passes through incorrectly when asked if want to add another product: choice = 4 passed through to "Enter the product id: " (also: Input of "1" allowed the "add another product to the cart?" query to continue on to adding another product to the cart, find why)
        - If a product_ID already exists in the cart, the additional quantity addition should sum to the original cart quantity after a user prompt to confirm addition with total quantity desired
    - Remove Cart Product
        - Fix the logic in remove_cartproduct since it can go from 'You must select a number of products that are less than...' straight to 'Product deleted from cart!' even if nothing is deleted
    - Do not require a password for Guest and delete the guest cart when logged out
    - Data validation for names, email addresses, etc.
    - Modularize for more efficient code
    - Change the 'list' currently defined for user permissions to a set (that is not a truple)
    - Define a new class for switch statements that includes methods for user and admin option menus
    - Eliminate redundancy logic to check if product ID exists in main() and user 'Add Cart Product' / admin 'Add product' options
    - Reduce 'repeat_choice_logic' code lines by implementing OR statements and other logic improvements
    - Inputs that convert to int() must have validation that a number was entered or the code will error out
    - Modify product in admin login should be able to choose which attributes they want to edit (i.e. product_name, category_id, price) rather than change all
    - Checking out with an empty cart pushes lots of errors likely due to the try catch. "An error occurred: local variable 'total' referenced before assignment"
    - Display lists when adding, modifying, deleting from the lists to help with knowing what you have in order to make changes
"""