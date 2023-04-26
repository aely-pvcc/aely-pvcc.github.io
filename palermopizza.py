# Name: Addison Ely
# Prog Purpose: This program creates a receipt for Palermo Pizza purchases
#   Sales tax rate: 5.5%

import datetime

########## define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = 0.055
PIZZA_SIZES = {
    "S": 9.99,
    "M": 12.99,
    "L": 14.99,
    "X": 17.99
}

# define global
num_pizzas = 0
subtotal = 0
sales_tax = 0
total = 0

# define program functions
def main():
    run_program = True
    while run_program:
        get_user_data()
        perform_calculation()
        display_results()
        another = input("Would you like to order another pizza? (Y/N): ")
        while another.lower() not in ['y', 'n']:
            print("Invalid input. Enter Y or N.")
            another = input("Would you like to order another pizza? (Y/N): ")
        if another.lower() == 'n':
            run_program = False
            print("Have a nice day!")

def get_user_data():
    global pizza_size
    pizza_size = input("Enter pizza size (S, M, L, X): ")
    while pizza_size.upper() not in PIZZA_SIZES:
        pizza_size = input("Invalid input. Enter pizza size (S, M, L, X): ")
    global num_pizzas
    num_pizzas = int(input("Enter number of pizzas: "))

def perform_calculation():     
    global pizza_cost
    #  Get the price of the selected pizza size
    pizza_price = PIZZA_SIZES[pizza_size.upper()]
    # Calculate the total cost of the pizzas ordered
    pizza_cost = pizza_price * num_pizzas
    global sales_tax
    sales_tax = pizza_cost * SALES_TAX_RATE
    global total
    total = pizza_cost + sales_tax
    
def display_results():
    print('--------------------PALERMO PIZZA-------------------')
    print('Address: 123 Main St., Charlottesville, VA')
    print('Phone: 555-545-5445')
    print('Pizza Size      : ' + str(pizza_size.upper()))
    print('Number of Pizzas: ' + str(num_pizzas))
    print('Pizza Cost      $ ' + format(pizza_cost, '8.2f'))
    print('Sales Tax       $ ' + format(sales_tax, '8.2f'))
    print('Total           $ ' + format(total, '8.2f'))
    print(str(datetime.datetime.now()))
    print("----------------------------------------------------")

# call on main program to execute
main()
