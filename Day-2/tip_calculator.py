print("Welcome to tip caclulator")

bill = float(input("What was the total bill? ₹"))
tip = int(input("What percentage would you like to give as tip (could not write '%' only write number) eg 10, 12, 15? "))
people= int(input("How many people to splite the bill? "))

total_tip_percentage = tip / 100
total_tip_amount = bill * total_tip_percentage
total_bill = bill + total_tip_amount
bill_per_people = total_bill / people
final_amount = round(bill_per_people, 2)

print(f"Each person should pay ₹{final_amount}")