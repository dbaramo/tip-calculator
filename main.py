#Greets customer
print("Welcome to the tip calculator!")

#Asks for total bill
bill = float(input("What was your bill total? \n"))

#Asks how much percent to tip
tip = int(input("How much percent tip you want to include? 10, 12, or 15\n"))

#Asks how much people to split the bill
num_people = int(input("How many people to split the bill\n"))

#Calculates bill with tip
bill_with_tip = tip / 100 * bill + bill

#Calculates how much each person has to pay
bill_per_person = round(bill_with_tip / num_people, 2)

#Format bill for print
amount = "{:.2f}".format(bill_per_person)

#Prints how much each persons share is
print(f"Each person should pay: ${amount}")