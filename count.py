range_numbers = 0
for z in range(1500, 2700):
    if z % 7 == 0 and  z % 5 == 0:
        print(z)
        range_numbers += 1
        print(range_numbers)