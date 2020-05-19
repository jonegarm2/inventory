stock ={'apples': 6, 'oranges': 3, 'pears': 0}
alreadyAte = []

food = input('Whatfood was eaten? ')
person = input('Who ate the food? ')

def menu():
    print("Press 1: To add stock. ")
    print("Press 2: To check stock. ")
    print("Press 3: To enter purchase. ")
    print("Press q: To add. ")
    return input("What would you like to do? ")

run = menu()

while True:
    if run == '1':
        addStock = input('Food to be added to stock? ')
        amount = int(input())