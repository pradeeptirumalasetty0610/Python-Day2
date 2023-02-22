print('Welcome to the tip calculator')
bill_amount=float(input('What was the total bill? $'))
tip_percent=int(input('What percentage tip would you like to give? '))
total_ppl=int(input('How many people to split the bill? '))

person_split=(bill_amount + (bill_amount*tip_percent)/100)/total_ppl

print(f'Each person should pay: ${round(person_split,2)}')