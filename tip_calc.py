print("Welcome to the tip  calculator")

bill = float(input("What was the total bill? PLN"))
tip = float(input(
    "What percentage tip would like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

each_person_should_pay_in_pln = round((bill / people * (tip / 100 + 1)), 2)
each_person_should_pay_in_eur = round(
    (each_person_should_pay_in_pln / 4.45), 2)

print(
    f"Each person should pay: \n PLN {each_person_should_pay_in_pln} \n EUR {each_person_should_pay_in_eur} ")
