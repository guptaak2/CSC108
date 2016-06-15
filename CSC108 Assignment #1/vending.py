# This program simulates a vending machine that gives change.

bill_str = input("Enter bill value (5 = $5 bill, 10 = $10 bill, etc.): ")
bill_pennies = int(bill_str) * 100
item_str = input("Enter item price in pennies: ")
item_pennies = int(item_str)

# Compute change due, in pennies
change = bill_pennies - item_pennies

# Determine the change returned
loonies = change // 100
change = change % 100
quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5
change = change % 5
pennies = change // 1

# Print the change returned
print("Loonies:", loonies) 
print("Quarters: ", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)

