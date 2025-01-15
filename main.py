# WELCOME TO CNUNO

import json
menu_db = 'menu.json'
admin_password = 'abcd'
waitor_password = '1234'

menu = {
    'Breakfast': {
        'Mashuni': 54,
        'Kulhimas': 53
        },
    'Italian': {
        'Carbonara': 54,
        'Pasta': 44
        },
    'Asian': {
        'Nasegoreng': 45
        },
    'Drinks': {
        'Coke': 43,
        'Fanta': 22
        }
}

def save_menu():
    try:
        with open(menu_db, 'w') as file:
            json.dump(menu, file, indent=4)
        print('Current menu has been saved to the database')
    except Exception as error:
        print(f'Menu could not be saved due to the following error: {e}')


def load_menu():
    global menu
    try:
        with open(menu_db, "r") as file:
            menu = json.load(file)
        print('Menu has been loaded from the database')
    except FileNotFoundError:
        print('DB file not found, using a new DB')
    except json.JSONDecodeError:
        print('Error reading the DB file')

def list_menu():
    print('These are the categories available: ')
    category = choose_category()
    print('Below are the items available in that category: ')
    print(list(menu[category].keys()))

def list_categories():
    for category in list(menu.keys()):
        print(category, end=', ')

def choose_category():
    list_categories()
    
    while True:
        try:
            chosen_category = input('\nPlease choose a category: ').title()
            if chosen_category not in list(menu.keys()):
                pass
            else:
                return chosen_category
        except:
            print('Not a valid category!')


def choose_item(category):
    print(list(menu[category].keys()))
    while True:
        try:
            chosen_item = input('Please choose an item: ').title()
            if chosen_item not in menu[category]:
                raise Exception
                pass
            else:
                return chosen_item
        except:
            print('Item not in list!')

def add_menu_item():
    ''
    # select category
    # enter name of item
    # enter price
    # show details and confirm


def remove_menu_item():
    for category in list(menu.keys()):
        print(category, end=', ')
    category = input('Please choose a category to remove from').title()
    if category in list(menu.keys()):
        print(menu[category])
        item_to_remove = input('Please choose an item to remove')
        if item_to_remove in menu[category]:
            yes_or_no = print(f'You are about to remove {item_to_remove} from {category}, do you wish to proceed? (Y/n): ')
            if yes_or_no == 'n':
                'go back'
            else:
                menu[category].pop(menu[category].index(item_to_remove))
                # print(menu[category])
                print(item_to_remove + ' has been removed from the menu!')
def edit_menu_item():
    ''






# remove_menu_item()

def validate_order_input():
    while True:
        ord = input('Please enter the name of the menu item to add to your order: ')
        if any(ord in menu[cat] for cat in menu):
            return ord
        else:
            print(ord + ' is not on the menu you blockhead!!')

def print_bill():
    bill_total = 0
    for item in current_order:
        bill_total += int(price_list[item])
    print('Total is MVR ' + str(bill_total))
    print('Would you like to proceed with the payment?')
    if proceed == 'y':
        calculate_payables()
    else:
        ''

def new_order():
        while True:
            ord = validate_order_input()
            current_order.append(ord)
            print(ord + ' has been added to the order!')
            print('Your current order is: ')
            print(str(current_order))
            cont = input('Would you like to add more items? (y/n): ')
            if cont != 'y':
                break;
        print('You order is: ' + str(current_order)) 
        print_bill()

def browse():
        list_menu()
        ready = input('Are you ready to order? (y/n)')
        if ready == 'y':
            new_order()
        elif ready == 'n':
            list_menu()
        else:
            print("Invalid response given, please enter 'y' or 'n'")
            browse()


# if admin:
def admin_menu():
    while True:
        print("--------------------")
        print('Welcome ADMIN!')
        print('1) Browse the menu')
        print('2) Add new menu item')
        print('3) Remove menu item')
        print('4) Edit menu item')
        print('5) Exit')

        choice = input('Please choose an option: ')
        if choice == '1':
            list_menu()
        elif choice == '2':
            add_menu_item()
        elif choice == '3':
            remove_menu_item()
        elif choice == '4':
            edit_menu_item()
        elif choice == '5':
            print('Exiting the admin menu..')
            break
        else:
            print('Invalid choice entered!')


# if waitor
def waitor_menu():
    while True:
        print("-------------------")
        print('Hello Waitor!')
        print('1) Browse the menu')
        print('2) Take an order')
        print('3) Billing')
        print('4) Exit')

        choice = input('Please choose an option: ')
        if choice == '1':
            list_menu()
        elif choice == '2':
            "take order"
        elif choice == '3':
            "generate bill"
        elif choice == '4':
            print('Exiting the waitor menu..')
            break
        else:
            print('Invalid choice entered!')


# if customer
def customer_menu():
    while True:
        print("-----------------------")
        print('1) Browse the menu')
        print('2) Rate our restaurant')
        print('3) Exit')

        choice = input('Please choose an option: ')
        if choice == '1':
            list_menu()
        elif choice == '2':
            "rate"
        elif choice == '3':
            print('Exiting..')
            break
        else:
            print('Invalid choice entered!')


## MAIN FUNCTION
current_order = []

print("--------------------------------------------------------------")
print('Greetings, Welcome to CNUNO! Home of "TOTALLY" original recipes!')

while True:
    # admin or waitor or customer
    try:
        print("----------------------------------")
        print('Please login:')
        user = input('1) Admin\n2) Waitor\n3) Customer')

        if user == '1':
            password = input('Enter the admin password: ')
            if password == admin_password:
                admin_menu()
                break;
            else:
                print('Invalid password entered!\n')
                raise Exception

        elif user == '2':
            password = input('Enter the waitor password: ')
            if password == waitor_password:
                waitor_menu()
                break;
            else:
                print('Invalid password entered!\n')
                raise Exception

        elif user == '3':
            customer_menu()
            break;

        elif user == '4':
            print(str(choose_item('Drinks')) + ' Will be removed')
            break
        
        else:
            print('Invalid user!!\n')
            raise Exception
    except:
        pass