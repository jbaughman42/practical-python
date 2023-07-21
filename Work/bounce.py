# bounce.py
#
# Exercise 1.5

height = 100
bounce = 0.6
num_bounces = 10
count = 1

while count <= 10:
    height = round(height * bounce, 4)
    print(f"{count}\t{height}")
    count += 1
