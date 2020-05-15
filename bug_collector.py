days = 0
running_total = 0

while days < 5:
    try:
        bugs =int(input("How many bugs have you collected on day?  "))
        running_total += bugs
        days += 1
    except:
        print("Please, enter numbers only!!")          
print("You have collected", running_total, "bugs in 5 days.")
    
