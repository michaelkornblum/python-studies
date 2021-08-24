my_list = [char.upper() for char in 'hello']
my_list2 = [number for number in sorted([8, 6, 7, 5, 3, 0, 9])]
my_list3 = [number ** 2 for number in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list4)