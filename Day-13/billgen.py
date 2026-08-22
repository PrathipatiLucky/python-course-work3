data = {
    'sugar' : 50,
    'salt' : 30,
    'chillipowder' : 70,
    'eggs' : 70,
    'peanuts' : 75,
    'rice' : 120,
}
for i in data:

    print(i.ljust(20),data[i])

prods = input("Enter the products: ").split()
print("----------Bill----------")
bill = 0
for i in prods:
        print(i.ljust(20),data[i])
        bill += data[i]
        print("Total bill".ljust(20),bill)