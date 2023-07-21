"""
sears.py
Created July 21, 2023 by Jennifer Baughman

Description:
"""

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

# Which line is the error? Line 15
# What is the error? days on one side of the statement should be day
# fix the error: done
# run successfully: done

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
