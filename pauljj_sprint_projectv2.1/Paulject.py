print ('paul jones, heck yeah')

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

    miles = float(input('Enter distance in miles: '))

    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))
#