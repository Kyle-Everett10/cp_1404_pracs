TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_used = int(input("Which tariff do you use? 11 or 31: "))
if tariff_used != 11 and tariff_used != 31:
    while tariff_used != 11 and tariff_used != 31:
        print("Invalid tariff, please input a valid tariff")
        tariff_used = int(input("Which tariff do you use? 11 or 31: "))

if tariff_used == 11:
    price_rate = TARIFF_11
elif tariff_used == 31:
    price_rate = TARIFF_31
daily_use = float(input("Enter your daily use in kWh: "))
billing_period = float(input("Enter number of billing days: "))
estimated_bill = price_rate * daily_use * billing_period
print("Estimated bill: ${:.2f}".format(estimated_bill))
