from random import randint

# Printing Menu
menu = [
    "Doritos",
    "Cheetos",
    "Lays",
    "Salad",  # 0-3 = Chips
    "Orange",
    "Mango",
    "Strawberry",
    "Choc Milk",  # 4-7 = Juices
    "Kinders",
    "Galaxy",
    "Ferrero Rocher",
    "Dairy Milk",  # 8-11 = Chocolates
    "Oreo",
    "Tate's Bake",
    "Toll House",
    "Delight",  # 12-15 = Cookies
    "Coca-Cola",
    "Pepsi",
    "Dew",
    "7-up",  # 16-19 = Soda
    "Tea",
    "Coffee",
    "Green Tea",
    "Black Coffee",  # 20-23 = Caffeine Drinks
    "Chocolate",
    "Kulfi",
    "Mango",
    "Vanilla",
]  # 24-27 = Ice Cream

addMoney = True

stock = [randint(0, 10) for i in range(28)]

menu_price = [
    3.75,
    3.00,
    2.45,
    1.50,
    2.50,
    3.75,
    4.00,
    4.25,
    2.80,
    2.00,
    5.00,
    3.25,
    4.00,
    6.00,
    5.25,
    4.20,
    3.00,
    4.20,
    4.25,
    3.55,
    4.00,
    5.00,
    3.75,
    4.25,
    2.25,
    2.00,
    1.50,
    1.00,
]

check = True

inventory = []

answer = "yes"

for i in range(len(menu)):
    if i == 0:
        print("Codes\tChips\t\tPrice\t\tStock")
    elif i == 4:
        print("Codes\tJuices\t\tPrice\t\tStock")
    elif i == 8:
        print("Codes\tChocolates\tPrice\t\tStock")
    elif i == 12:
        print("Codes\tCookies\t\tPrice\t\tStock")
    elif i == 16:
        print("Codes\tSoda\t\tPrice\t\tStock")
    elif i == 20:
        print("Codes\tCaffeine/Drinks\tPrice\t\tStock")
    elif i == 24:
        print("Codes\tIce Cream\tPrice\t\tStock")
    if i == 0 or i == 2 or i == 5:
        print(f"{i}:\t{menu[i]}\t\t{menu_price[i]} dhs\t{stock[i]}")
    elif i == 6 or i == 10 or i == 13 or i == 16:
        print(f"{i}:\t{menu[i]}\t{menu_price[i]} dhs\t\t{stock[i]}")
    elif i == 18 or i == 19:
        print(f"{i}:\t{menu[i]}\t\t{menu_price[i]} dhs\t{stock[i]}")
    elif len(menu[i]) <= 8:
        print(f"{i}:\t{menu[i]}\t\t{menu_price[i]} dhs\t\t{stock[i]}")
    else:
        print(f"{i}:\t{menu[i]}\t{menu_price[i]} dhs\t{stock[i]}")
    if (i + 1) % 4 == 0:
        print("\n")
money = 0
while answer.lower() == "yes":
    if addMoney == True:
        try:
            print(f"Current Money: {money}")
            money = float(input("Enter the money: "))
            while money < 0:
                money = float(input("Error!\nEnter money again: "))
        except:
            while check == True or money < 0:
                try:
                    money = float(input("Error!\nEnter money again: "))
                    check = False
                except:
                    check = True
    money += addMoney
    check = True
    try:
        choice = int(input("Enter your choice: "))
        while choice < 0 and choice > 27:
            money = int(input("Error!\nEnter choice again: "))
    except:
        while check == True or (choice < 0 or choice > 27):
            try:
                choice = int(input("Error!\nEnter choice again: "))
                check = False
            except:
                check = True
    inventory.append(menu[choice])
    if money >= menu_price[choice]:
        if stock[choice] >= 1:
            addMoney = False
            money -= menu_price[choice]
            answer = input("You want to buy more things?(yes/no): ")
            while answer.lower() != "yes" and answer.lower() != "no":
                answer = input("You want to buy more things?(yes/no): ")
            if answer.lower() == "no":
                print(f"Your change is: {round(money,3)} dhs")
                print("Following item(s) has been dispensed")
                for i in range(len(inventory)):
                    print(f"\t{i+1}. {inventory[i]}")
        else:
            print("This item is out of stock.")
    else:
        print("You're short on money.")
        addMoney = True