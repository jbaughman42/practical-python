# mortgage.py
#
# Exercise 1.7
# Exercise 1.9 answer: 880,074.10 over 310 months

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
month = 0
extra = 1000
extra_start = 61
extra_end = 108

while principal > 0:
    month += 1
    if extra_start <= month <= extra_end:
        payment = base_payment + extra
    else:
        payment = base_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    
print(f"Total Paid: {total_paid:,.2f} over {month} months")
