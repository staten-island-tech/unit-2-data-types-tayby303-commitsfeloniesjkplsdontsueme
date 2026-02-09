service=input("Was the service great, good, okay, or bad? ")
if service=="great":
    bill=("25%")
elif service=="good":
    bill=("20%")
elif service=="okay":
    bill=("15%")
elif service=="bad":
    bill=("0%")
print("The tip will be "+bill)