# WELCOME TO CNUNO


menu = {
    'Breakfast': ['Mashuni', 'Kulhimas'],
    'Italian': ['Carbonara'],
    'Asian': ['Nasegoreng'],
    'Drinks': ['Coke', 'Fanta']
}
def list_menu():
    for menu_item in menu:
        print(f'{menu_item}: {str(menu[menu_item])}')

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

remove_menu_item()