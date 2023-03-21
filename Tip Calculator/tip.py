print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
total_people = input("How many people to split the bill? ")
tip_per = input("What percentage of tip would you like to give? 10, 12, or 15? ")
tip_amt =  float(total_bill)*int(tip_per)/100
payable_amt = tip_amt +  float(total_bill)
each_per = round(payable_amt/int(total_people),2)

print(each_per)