# WELCOME TO CNUNO

import json, random
menu_db = 'menu.json'
keys = {}
menu = {}
tables = {}
tax = 0.08 # %

## DEFINE THE FUNCTIONS

## MENU RELATED
def save_menu():
    try:
        with open(menu_db, 'w') as file:
            json.dump(menu, file, indent=4)
        print('Current menu has been saved to the database!')
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
    for item in menu[category]:
        print(f'{item}: MVR {menu[category][item]}')
    input('Press enter to continue..')

def add_menu_item():
    # select category
    category = choose_category()
    # enter name of item
    new_item = input('Please enter the name of the new item to add: ')
    # enter price
    new_item_price = input('Please enter the price for ' + new_item)
    # show details and confirm
    print(f'{new_item} costing MVR {new_item_price} will be added to {category}')
    confirm = input('Proceed? (y/n): ')
    if confirm == 'y':
        menu[category][new_item] = int(new_item_price)
        input('Successfully added! Press enter to return..')

def remove_menu_item():
    category = choose_category()
    item_to_remove = choose_item(category, 'Please choose an item to remove: ')

    confirmation = input(f'You are about to remove {item_to_remove} from the menu, do you wish to proceed? (y/N): ')
    if confirmation == 'y':
        del menu[category][item_to_remove]
        print(list(menu[category].keys()))
        print(item_to_remove + ' has been removed from the menu!')
    else:
        input('Cancelled! Press enter to return to admin menu..')

def edit_menu_item():
    category = choose_category()
    item_to_edit = choose_item(category, 'Please choose an item to edit: ')

    choice = input('1) Edit name\n2) Edit price\nChoose an option: ')
    if choice == '1':
        new_name = input('Enter new name: ')
        menu[category][new_name] = menu[category].pop(item_to_edit)
        print(f'{item_to_edit} has successfully been renamed to {new_name}')
        input('Press enter to return..')
    elif choice == '2':
        new_price = int(input('Enter new price (MVR): '))
        menu[category][item_to_edit] = new_price
        print(f'The price for {item_to_edit} has successfully been changed to {new_price}')
        input('Press enter to return..')

## ITEM RELATED
def choose_category():
    for category in list(menu.keys()):
        print(category, end=', ')

    while True:
        try:
            chosen_category = input('\nPlease choose a category: ').title()
            if chosen_category not in list(menu.keys()):
                pass
            else:
                return chosen_category
        except:
            print('Not a valid category!')

def choose_item(category, prompt):
    print(list(menu[category].keys()))
    while True:
        try:
            chosen_item = input(prompt).title()
            if chosen_item not in menu[category]:
                raise Exception
                pass
            else:
                return chosen_item
        except:
            print('Item not in list!')


## ORDER RELATED
def take_order():
    table_number = input('Enter the table number: ')
    if table_number not in tables:
        tables[table_number] = []

    while True:
        order_item = input("Please choose an item to order, (Type 'finish' to complete ordering): ").title()

        if order_item == 'Finish':
            print('Finishing up..')
            break

        for category, item in menu.items():
            if order_item in item:
                try:
                    qty = int(input('Enter the quantity of the item to order: '))

                    if qty <= 0:
                        print('Quantity must be atleast one!')
                        continue

                    tables[table_number].append([order_item, qty])
                    print(f'Successfully added {qty}x {order_item} to table {table_number} order!')
                    break

                except ValueError:
                    print("Invalid quantity. Please enter a number.")
                break
        else:
            print('Item not in list or quantity error!')

    print(tables)

def print_bill():
    bill_total = 0
    invoice_num = random.randrange(1000, 5000)

    table_number = input('Enter the table number: ')
    if table_number not in tables:
        print('Selected table is empty!')
        return
    
    f = open(f"invoices/invoice_{invoice_num}.txt", "x")

    f.write(f"\nCNUNO Invoice #{invoice_num} [TB: {table_number}]")
    f.write("\n---------------------------")

    for order_item, qty in tables[table_number]:
        for category, menu_items in menu.items():
            if order_item in menu_items:
                price = menu_items[order_item] * qty
                bill_total += price
                f.write(f"\n{qty}x {order_item}: MVR {price:.2f}")
                break
    
    tax_charge = tax * bill_total
    f.write("\n---------------------------")
    f.write(f'\nSubtotal: MVR {bill_total:.2f}')
    f.write(f'\nGST (8%): MVR {tax_charge:.2f}')
    f.write(f'\nTOTAL: MVR {(bill_total + tax_charge):.2f}')
    f.write("\n---------------------------")

    f.close()

    f = open(f"invoices/invoice_{invoice_num}.txt", "r")
    print(f.read())
    f.close()

    input('Press enter to continue..')
    

## USER MENU RELATED
# if admin:
def admin_menu():
    while True:
        print("--------------------")
        print('Welcome ADMIN!')
        print('1) Browse the menu')
        print('2) Add item')
        print('3) Remove item')
        print('4) Edit item')
        print('5) Save current menu')
        print('6) Exit')

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
            save_menu()
        elif choice == '6':
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
            take_order()
        elif choice == '3':
            print_bill()
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



## INIT
print('-- PROGRAM INITIALIZING :D --')
try:
    with open('keys.json', "r") as file:
        keys = json.load(file)
    print('Passwords have been loaded from keys file')
except json.JSONDecodeError:
    print('Error reading the keys file')


admin_password = keys["admin_password"]
waitor_password = keys["waitor_password"]

current_order = []
load_menu()
print('-- INITIALIZATION COMPLETE! :D --')


## MAIN FUNCTION
print("================================================================")
print('Greetings, Welcome to CNUNO! Home of "TOTALLY" original recipes!')
print("================================================================")

while True:
    # admin or waitor or customer
    try:
        print("--------------")
        print('Please login:')
        user = input('1) Admin\n2) Waitor\n3) Customer\n4) Exit\nChoose a user: ')

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
            break
        
        else:
            print('Invalid user!!\n')
            raise Exception
    except:
        pass