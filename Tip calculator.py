print("Welcome to the tip calculator!")

total = float(input("What was the total bill?\n $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15?\n %"))

people = int(input("How many people to split the bill?\n "))

tip_calculation = tip / 100 * total + total

split_total = tip_calculation / people

rounded = round(split_total, 2)

message = f"Each person should pay:\n ${rounded}"

print(message)
