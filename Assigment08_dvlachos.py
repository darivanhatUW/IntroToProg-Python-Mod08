# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# DVlachos,3.9.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
str_file_name = 'products.txt'
str_choice = ""
lst_of_product_objects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    def __init__(self, product_name, product_price):
        # 	   -- Attributes --
        self.product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers.")

    @property
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price).title()  # Title case

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ', $' + self.product_price


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DVlachos,3.9.2021,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file):
        list = []
        file = open(file, "r")
        for line in file:
            products = line.split(",")
            row = Product(products[0], products[1])
            list.append(row)
        file.close()
        return lst_of_product_objects

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name: str, list_of_products: list):
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_products:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("Your file was not saved due to a general order.")
            print(e, e.__doc__, type(e), sep="\n")
        return success_status


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Presents data to and from a a list of product objects:

    methods:
        display_menu(): (string) with menu of choices
        input_menu_choice(): (strings) input from user to select menu item
        print_current_file_data(): returns list of products and prices
        add_product_data(): prompts for user input of products and prices

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DVlachos,3.7.2021,Modified code to complete assignment 8
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def display_menu():
        print(
            '''
        1) See current list of products
        2) Add product to list
        3) Save to file
        4) Exit
        ''')

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = int(input("Which option would you like to perform? [1 to 3] - "))
        print()  # Added extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_list_of_product():
        print("Product List:")
        print("---------------------")
        for row in list_of_product_objects:
            print(row.product_name + ": " + row.product_price)
        print()  # Add for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def add_product_data():
        user_product_name = input("Enter product: ")
        user_product_price = input("Enter price: $")
        print()  # Added extra line for looks
        product = Product(user_product_name, user_product_price)
        return product


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
list_of_product_objects = FileProcessor.read_data_from_file(str_file_name)

while True:
    IO.display_menu()  # Show user a menu of options
    str_choice = IO.input_menu_choice()  # Get user's menu option choice

    if str_choice == 1:  # Show user current data in the list of product objects
        IO.print_list_of_product()
        continue

    elif str_choice == 2:  # Let user add data to the list of product objects
        list_of_product_objects.append(IO.add_product_data())
        continue

    elif str_choice == 3:  # let user save current data to file and exit program
        FileProcessor.save_data_to_file(str_file_name, list_of_product_objects)
        print("Your entries have been saved.")
        continue

    elif str_choice == 4:
        break

# Main Body of Script  ---------------------------------------------------- #
