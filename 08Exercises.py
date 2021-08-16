# 8.10. Exercises: Lists

line_start = '\n<--------'
line_end = '-------->'

# part = '8.10.1. Part One: Adding and Removing Items'
# print(line_start, part, line_end)

# adding_practice = [273.15]
# print(f'Start: {adding_practice}')
# adding_practice.append(42)
# adding_practice.append("hello")
# print(f'1: {adding_practice}')

# adding_practice += [False, -4.6, '87']
# print(f'2: {adding_practice}')

# cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']
# print(f'\nOriginal Cargo: {cargo_hold}')
# cargo_hold[cargo_hold.index('slinky')] = 'space tether'
# print(f'Current Cargo: {cargo_hold}')
# print(f'Removed: {cargo_hold.pop(-1)}')
# print(f'Current Cargo: {cargo_hold}')
# print(f'Removed: {cargo_hold.pop(0)}')
# print(f'Current Cargo: {cargo_hold}')
# cargo_hold.insert(0, 1138)
# cargo_hold.append('20 meters')
# print(f'Current Cargo: {cargo_hold}')
# print('Removed: parrot')
# cargo_hold.remove('parrot')
# print(f'Current Cargo: {cargo_hold}')
# final_text = "\nThe list {0} contains {1} items."
# print(final_text.format(cargo_hold, len(cargo_hold)))

# part = '8.10.2. Part Two: Slices & Methods'
# print(line_start, part, line_end)

# cargo_hold[3:3] = ['keys']
# print(f'1a. Current Cargo: {cargo_hold}')
# remove_index = cargo_hold.index('instruction manual')
# cargo_hold = cargo_hold[:remove_index] + cargo_hold[remove_index+1:]
# print(f'1b. Current Cargo: {cargo_hold}')
# cargo_hold[2:5] = ['cat', 'book', 'string cheese']
# print(f'1c. Current Cargo: {cargo_hold}')

# supplies_1 = ['duct tape', 'gum', 3.14, False, 6.022e23]
# supplies_2 = ['orange drink', 'nerf toys', 'camera', '42', 'Rutabaga']

# print(f'Original supplies_1:\t{supplies_1}')
# print(f'Slice of last 3 items:\t{supplies_1[-3:]}')
# print(f'Current supplies_1:\t{supplies_1}')

# supplies_1.reverse()
# print(f'\nOriginal supplies_1:\t{supplies_1}')
# print(f'Reversed supplies_1:\t{supplies_1}')
# print(f'Original supplies_2:\t{supplies_2}')
# supplies_2.sort()
# print(f'Sorted supplies_2:\t{supplies_2}')

# print('\nThe difference between reverse() and sort() is that reverse() doesn\'t alter the original string while sort() does.')

# part = '8.10.3. Part Three: Split, List, and Join'
# print(line_start, part, line_end)

# phrase = 'In space, no one can hear you code.'
# print(f'\n{phrase}\n')
# print(phrase.split())
# print()
# print(phrase.split('e'))
# print()
# print(list(phrase))
# my_list = ['B', 'n', 'n', 5]
# print(f'\n{my_list}\n')
# print("''.join(my_list) vs. 'a'.join(my_list) vs. '_'.join(my_list)")
# print("""
# Trying to do any of the above three joins causes an error because it's trying to join 
# an integer to a string and it's the wrong data type.

# The purpose of the argument inside the () for string.join() is to tell where the string should be joined at. 
# That is, the string should be joined in between each element of the array/list 
#     i.e. ''.join(['cat', 'dog']) would return 'catdog'
# """)

# a_list = 'water,space suits,food,plasma sword,batteries'.split(',')
# a_list.sort()
# print('-'.join(a_list))

part = '8.10.4. Part Four: Multi-dimensional Lists'
print(line_start, part, line_end)

