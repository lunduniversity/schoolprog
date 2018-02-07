# Part A

def amount_with_rate(time, starting_amount, rate):
    total = starting_amount * (rate ** time)
    return total


# Part B

print(amount_with_rate(10, 100, 0.6))


# Part C

def rate_comparison(time, starting_amount, rate_1, rate_2):
    bank_1 = amount_with_rate(time, starting_amount, rate_1)
    bank_2 = amount_with_rate(time, starting_amount, rate_2)

    if bank_1 > bank_2:
        print("Bank 1 is the better choice")
        return bank_1
    else:
        print("Bank 2 is the better choice")
        return bank_2

rate_comparison(2, 400, 0.5, 0.8)
