def print_menu():
    try:
        print('1. kilograms to pounds')
        print('2. pounds to kilograms') 

if __name__ == '__main__':
    print_menu()
    choice = input('Which would you like to do today?: ')
    if choice == '1':
        kg_pound()
    if choice == '2':
        pound_kg()
    else:
        print("Please pick one between option 1 and option 2.")