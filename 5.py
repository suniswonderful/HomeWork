revenue = int(input('Enter revenue: '))
outgoings = int(input('Enter outgoings: '))
if revenue > outgoings:
    income = revenue - outgoings
    efficiency = income / revenue
    print('Your company is profitable')
    print('Your efficiency is {}'.format(efficiency))
    workers_amount = int(input("Enter your workers' amount: "))
    every_worker = income / workers_amount
    print('Income for each worker is {}'.format(every_worker))
elif revenue < outgoings:
    print("Sorry, your company is unprofitable. Try harder. You're in danger")
if revenue == outgoings:
    print('Your revenue covers your outgoings, but unfortuneately you have no income')
