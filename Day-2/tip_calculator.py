print("Welcome to tip caclulator")

bill = float(input("What was the total bill? ₹")) 

tip = int(input("What percentage would you like to give as tip (couldn't write the '%' symbol, only the number.) eg 10, 12, 15? "))
person= int(input("How many person to splite the bill? "))

total_tip_percentage = tip / 100
total_tip_amount = bill * total_tip_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / person
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ₹{final_amount}")
