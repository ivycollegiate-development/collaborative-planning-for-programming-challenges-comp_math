def kg_pound():
    try:
        kg = float(input('Please enter the weight in kilograms: '))
        pound = kg/0.45359237
        print(pound, 'pounds')
        print("Fun fact: ",random.choice(weight_facts))
    except ValueError:
        print("Try again. Please enter a valuable number.")
        return None
def pound_kg():
    try:
        pound = float(input('Please entr the weight in pound: '))
        kg = pound*0.45359237
        print(kg, 'kg')
        print("Fun fact: ",random.choice(weight_facts))
    except ValueError: 
        print("Try again. Please enter a valuable number.")
        return None