bill = float(input("Input the total amount of your check: "))
tip = int(input("How much tip would you like to give? 10, 15, 20? "))
people = int(input("How many people are in your group? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")