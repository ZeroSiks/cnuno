# WELCOME TO CNUNO


menu = {
    'Breakfast': ['Mashuni', 'Kulhimas'],
    'Italian': ['Carbonara'],
    'Asian': ['Nasegoreng'],
    'Drinks': ['Coke', 'Fanta']
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


## MAIN FUNCTION
current_order = []

print('Greetings, welcome to our automated order tracking app!')
# browse menu
boo = input('Would you like to:\n1) Browse our menu\n2) Place an order\nbrowse / order: ')

if boo == 'browse':
    list_menu()
    print('Are you ready to order?')
elif boo == 'order':
    # choose menu item:
    while True:

        ord = input('Please enter the name of the menu item to add to your order: ')
        if any(ord in menu[cat] for cat in menu):
            current_order.append(ord)
            print(ord + ' has been added to the order!')
        else:
            print(ord + ' is not on the menu you blockhead!!')

        print('Your current order is: ')
        print(str(current_order))
        cont = input('Would you like to add more items? (y/n): ')
        if cont != 'y':
            break;
    print('You order is: ' + str(current_order))
    print('Total is $921')
            # ask if additional items are needed
            # if 1:
            # add to order again

            # if 2: finalize order()
            # confirm order
            #print_order()
            # your total is $$$



# add_to_order(choose_menu_item())

# elif 2:
# add_to_order(choose_menu_item())
