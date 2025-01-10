# WELCOME TO CNUNO


menu = {
    'Breakfast': ['Mashuni', 'Kulhimas'],
    'Italian': ['Carbonara'],
    'Asian': ['Nasegoreng'],
    'Drinks': ['Coke', 'Fanta']
}

price_list = {
    'Mashuni': '24',
    'Kulhimas': '55',
    'Carbonara': '64',
    'Nasegoreng': '24',
    'Coke': '92',
    'Fanta': '100'
}


def list_menu():
    print('These are the categories available: ')
    for category in list(menu.keys()):
        print(category, end=', ')
    category = input('\nCategory name: ').title()
    if category in list(menu.keys()):
        print('Below are the items available in that category: ')
        print(menu[category])

        
    # for menu_item in menu:
    #     print(f'{menu_item}: {str(menu[menu_item])}')

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
    print('Total is MVR' + str(bill_total))

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
        ready = input('Are you ready to order?')
        if ready == 'y':
            new_order()
        elif ready == 'n':
            list_menu()
        else:
            print("Invalid response given, please enter 'y' or 'n'")
            browse()


## MAIN FUNCTION
current_order = []

print('Greetings, welcome to our automated order tracking app!')
# browse menu

while True:
    # user selection menu on start:
    # users are admin, waitor, customer



    boo = input('Would you like to:\n1) Browse our menu\n2) Place an order\nEnter number 1-2: ')

    if boo == '1':
        browse()
        break
    elif boo == '2':
        # choose menu item:
        new_order()
        break
    else:
        print('Invalid number entered!\n')




# add_to_order(choose_menu_item())

# elif 2:
# add_to_order(choose_menu_item())
