def atm_withdrawal(balance, amount):
    if amount > balance:
        return "Insufficient founds", balance
    elif amount <= 0:
        return "Invalid amount", balance
    else:
        balance -= amount
        return "Transaction successful", balance

# Unit testing   
# print(atm_withdrawal(100,150)) --> with this is a lot time consuming because you need to manually input data

# CHECK test_atm.py file

