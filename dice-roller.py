import random

print("Select your die.")
print("Die: d4, d6, d8, d10, d12, d20")

while True:
    choice = input("Enter choice(d4/d6/d8/d10/d12/d20): ")

    number = input("How many dice: ")

    d4 = random.randint(1, 4)
    d6 = random.randint(1, 6)
    d8 = random.randint(1, 8)
    d10 = random.randint(1, 10)
    d12 = random.randint(1, 12)
    d20 = random.randint(1, 20)

    if choice == 'd4':
        print (d4)
       
    elif choice == 'd6':
        print (d6)
      
    elif choice == 'd8':
        print (d8)
      
    elif choice == 'd10':
        print (d10)
      
    elif choice == 'd12':
        print (d12)
      
    elif choice == 'd20':
        print (d20)
      
    next_roll = input("Want another roll? (yes/no): ")
    if next_roll == 'no':
        break
      
    else:
        print("Invalid Input")