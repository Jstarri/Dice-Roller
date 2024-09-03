import random

def d4():
    d_number = int(input("How many dice do you want to roll?"))
    d_4 = [random.randint(1, 4) for x in range(d_number)]
    print (d_4)

def d6():
    d_number = int(input("How many dice do you want to roll?"))
    d_6 = [random.randint(1, 6) for x in range(d_number)]
    print (d_6)

def d8():
    d_number = int(input("How many dice do you want to roll?"))
    d_8 = [random.randint(1, 8) for x in range(d_number)]
    print (d_8)

def d10():
    d_number = int(input("How many dice do you want to roll?"))
    d_10 = [random.randint(1, 10) for x in range(d_number)]
    print (d_10)

def d12():
    d_number = int(input("How many dice do you want to roll?"))
    d_12 = [random.randint(1, 12) for x in range(d_number)]
    print (d_12)

def d20():
    d_number = int(input("How many dice do you want to roll?"))
    d_20 = [random.randint(1, 20) for x in range(d_number)]
    print (d_20)

def d100():
    d_number = int(input("How many dice do you want to roll?"))
    d_100 = [random.randint(1, 100) for x in range(d_number)]
    print (d_100)

print("Select your die.")
print("Die: d4, d6, d8, d10, d12, d20, d100")

while True:
    choice = input("Enter choice(d4/d6/d8/d10/d12/d20/d100): ")

    if choice == 'd4':
        d4()
       
    elif choice == 'd6':
        d6()
      
    elif choice == 'd8':
        d8()
      
    elif choice == 'd10':
        d10()
      
    elif choice == 'd12':
        d12()
      
    elif choice == 'd20':
        d20()
    
    elif choice == 'd100':
        d100()
      
    next_roll = input("Want another roll? (yes/no): ")
    if next_roll == 'no':
        print("Thank you!")
        break