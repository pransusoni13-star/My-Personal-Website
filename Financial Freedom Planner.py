print("=" * 70)
print("         CANADIAN FINANCIAL FREEDOM CALCULATOR")
print("=" * 70)

name = input("\nWhat is your name? ")
age = int(input("How old are you? "))
retirement_age = int(input("What age do you want to retire? "))

salary = float(input("\nAnnual Salary ($): "))
spouse_salary = float(input("Spouse Annual Salary ($, 0 if none): "))
province = input("Province (ON, BC, AB, etc.): ")

total_income = salary + spouse_salary

tax_rate = float(input("\nEstimated Tax Rate (%): "))
after_tax_income = total_income * (1 - tax_rate / 100)

monthly_expenses = float(input("\nMonthly Living Expenses ($): "))
annual_expenses = monthly_expenses * 12

tfsa = float(input("\nCurrent TFSA Balance ($): "))
fhsa = float(input("Current FHSA Balance ($): "))
rrsp = float(input("Current RRSP Balance ($): "))
resp = float(input("Current RESP Balance ($): "))
hysa = float(input("Current HYSA Balance ($): "))
brokerage = float(input("Current Brokerage Balance ($): "))
other = float(input("Other Investments ($): "))

total_assets = tfsa + fhsa + rrsp + resp + hysa + brokerage + other

debt = float(input("\nTotal Debt ($): "))
net_worth = total_assets - debt

tfsa_contribution = float(input("\nAnnual TFSA Contribution ($): "))
fhsa_contribution = float(input("Annual FHSA Contribution ($): "))
rrsp_contribution = float(input("Annual RRSP Contribution ($): "))
resp_contribution = float(input("Annual RESP Contribution ($): "))
brokerage_contribution = float(input("Annual Brokerage Contribution ($): "))

annual_savings = (
    tfsa_contribution +
    fhsa_contribution +
    rrsp_contribution +
    resp_contribution +
    brokerage_contribution
)

rrsp_percent = (rrsp_contribution / salary) * 100 if salary > 0 else 0
resp_percent = (resp_contribution / salary) * 100 if salary > 0 else 0
tfsa_percent = (tfsa_contribution / salary) * 100 if salary > 0 else 0
fhsa_percent = (fhsa_contribution / salary) * 100 if salary > 0 else 0
brokerage_percent = (brokerage_contribution / salary) * 100 if salary > 0 else 0

savings_rate = (annual_savings / total_income) * 100 if total_income > 0 else 0

passive_income = float(input("\nAnnual Passive Income ($): "))

capital_gains = float(input("Expected Annual Capital Gains ($): "))
taxable_capital_gains = capital_gains * 0.50

expected_return = float(input("Expected Annual Investment Return (%): "))

years_left = retirement_age - age

freedom_number = annual_expenses * 25
freedom_percent = min((net_worth / freedom_number) * 100, 100) if freedom_number > 0 else 0

emergency_goal = monthly_expenses * 6
money_left = after_tax_income - annual_expenses

projected_value = total_assets

for year in range(years_left):
    projected_value = projected_value * (1 + expected_return / 100)
    projected_value += annual_savings

print("\n" + "=" * 70)
print("                    FINANCIAL DASHBOARD")
print("=" * 70)

print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Retirement Age Goal: {retirement_age}")
print(f"Years Until Retirement: {years_left}")

print("\nINCOME")
print(f"Gross Income: ${total_income:,.2f}")
print(f"Estimated Tax Rate: {tax_rate:.1f}%")
print(f"After-Tax Income: ${after_tax_income:,.2f}")

print("\nEXPENSES")
print(f"Monthly Expenses: ${monthly_expenses:,.2f}")
print(f"Annual Expenses: ${annual_expenses:,.2f}")

print("\nNET WORTH")
print(f"Total Assets: ${total_assets:,.2f}")
print(f"Debt: ${debt:,.2f}")
print(f"Net Worth: ${net_worth:,.2f}")

print("\nINVESTMENT ACCOUNTS")
print(f"TFSA: ${tfsa:,.2f}")
print(f"FHSA: ${fhsa:,.2f}")
print(f"RRSP: ${rrsp:,.2f}")
print(f"RESP: ${resp:,.2f}")
print(f"HYSA: ${hysa:,.2f}")
print(f"Brokerage: ${brokerage:,.2f}")
print(f"Other Investments: ${other:,.2f}")

print("\nANNUAL CONTRIBUTIONS")
print(f"TFSA: ${tfsa_contribution:,.2f} ({tfsa_percent:.1f}% of salary)")
print(f"FHSA: ${fhsa_contribution:,.2f} ({fhsa_percent:.1f}% of salary)")
print(f"RRSP: ${rrsp_contribution:,.2f} ({rrsp_percent:.1f}% of salary)")
print(f"RESP: ${resp_contribution:,.2f} ({resp_percent:.1f}% of salary)")
print(f"Brokerage: ${brokerage_contribution:,.2f} ({brokerage_percent:.1f}% of salary)")

print("\nCANADIAN CONTRIBUTION LIMITS")
print("TFSA Annual Limit: $7,000")
print("FHSA Annual Limit: $8,000")
print("FHSA Lifetime Limit: $40,000")
print("RRSP Limit: 18% of earned income")
print("RESP Lifetime Limit: $50,000 per child")
print("Brokerage: Unlimited")

print("\nSAVINGS")
print(f"Annual Savings: ${annual_savings:,.2f}")
print(f"Savings Rate: {savings_rate:.1f}%")

print("\nEMERGENCY FUND")
print(f"Goal (6 Months): ${emergency_goal:,.2f}")
print(f"Current HYSA: ${hysa:,.2f}")

if hysa >= emergency_goal:
    print("Status: Complete")
else:
    print(f"Need: ${emergency_goal - hysa:,.2f}")

print("\nPASSIVE INCOME")
print(f"Annual Passive Income: ${passive_income:,.2f}")

if passive_income >= annual_expenses:
    print("Status: Covers Living Expenses")
else:
    print(f"Need: ${annual_expenses - passive_income:,.2f} More")

print("\nBROKERAGE TAX SUMMARY")
print(f"Capital Gains: ${capital_gains:,.2f}")
print(f"Taxable Capital Gains: ${taxable_capital_gains:,.2f}")

print("\nMONEY AVAILABLE")
print(f"Money Left After Taxes & Expenses: ${money_left:,.2f}")

print("\nFINANCIAL FREEDOM")
print(f"Financial Freedom Number: ${freedom_number:,.2f}")
print(f"Progress: {freedom_percent:.1f}%")

bars = int(freedom_percent // 5)
progress_bar = "█" * bars + "░" * (20 - bars)
print(progress_bar)

if freedom_percent < 20:
    print("Level: Beginner")
elif freedom_percent < 40:
    print("Level: Building Wealth")
elif freedom_percent < 60:
    print("Level: Strong Saver")
elif freedom_percent < 80:
    print("Level: Nearly Financially Free")
elif freedom_percent < 100:
    print("Level: Almost There")
else:
    print("Level: FINANCIALLY FREE")

print("\nRETIREMENT PROJECTION")
print(f"Expected Return: {expected_return:.1f}%")
print(f"Projected Portfolio at Age {retirement_age}: ${projected_value:,.2f}")

score = 0

if savings_rate >= 20:
    score += 20
elif savings_rate >= 10:
    score += 10

if hysa >= emergency_goal:
    score += 20

if debt == 0:
    score += 20
elif debt < total_assets * 0.25:
    score += 10

if freedom_percent >= 50:
    score += 20
elif freedom_percent >= 25:
    score += 10

if passive_income >= annual_expenses:
    score += 20
elif passive_income >= annual_expenses * 0.5:
    score += 10

print("\nFINANCIAL HEALTH SCORE")

if score >= 90:
    rating = "Excellent"
elif score >= 75:
    rating = "Very Good"
elif score >= 60:
    rating = "Good"
elif score >= 40:
    rating = "Fair"
else:
    rating = "Needs Improvement"

print(f"Score: {score}/100")
print(f"Rating: {rating}")

print("\nRECOMMENDATIONS")

if savings_rate < 20:
    print("- Increase savings rate to 20% or more.")

if debt > 0:
    print("- Pay down debt faster.")

if hysa < emergency_goal:
    print("- Build your emergency fund.")

if rrsp_percent < 10:
    print("- Increase RRSP contributions.")

if tfsa_contribution < 7000:
    print("- Maximize your TFSA.")

if fhsa_contribution < 8000:
    print("- Maximize your FHSA.")

if passive_income < annual_expenses:
    print("- Grow passive income sources.")

print("\nKeep investing consistently and building wealth!")
print("=" * 70)