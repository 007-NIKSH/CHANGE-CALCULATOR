change = 0
i = 0
denom_array = [2000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
amount = int(input("ENTER THE COST OF YOUR ITEMS: "))
balance = int(input("ENTER THE AMOUNT PAID: "))
 
if amount <= balance:
  change = balance - amount
  rem = change
  print("\nYOUR CHANGE IS RS", rem, "\n")
 
  while(rem > 0):
    denom = rem // denom_array[i]
    
    if(denom != 0):
      print("YOUR Rs", denom_array[i], "NOTES ARE" , denom)
    
    rem = rem % denom_array[i]
    i = i + 1