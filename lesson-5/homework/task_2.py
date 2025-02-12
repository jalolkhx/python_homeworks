def invest(amount, rate, years) :
    for i in range(1, years+1) :
        amount += amount*rate
        print(f"year {i}: ${amount:.2f}")

DepositAmount = float(input("Enter your Deposit amount in $: "))
AnnualRate = float(input("Choose the annual rate: "))
Duration = int(input("Enter the period in years: "))
invest(DepositAmount, AnnualRate, Duration)