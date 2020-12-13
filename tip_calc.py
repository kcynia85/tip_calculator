print("Welcome to the tip  calculator")

total_bill = input("What was the total bill in PLN? ")
percentage_tip = input(
    "What percentage tip would like to give? 10, 12 or 15? ")
number_of_people = input("How many people to split the bill? ")

each_person_should_pay_in_pln = round(
    (float(total_bill) / int(number_of_people)) * (float(percentage_tip) / 100 + 1), 2)

each_person_should_pay_in_eur = round(each_person_should_pay_in_pln / 4.45, 2)
print(
    f"Each person should pay: \n PLN {each_person_should_pay_in_pln} \n EUR {each_person_should_pay_in_eur} ")
