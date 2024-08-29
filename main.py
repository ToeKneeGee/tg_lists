import sys
import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(f"len(numbers) = {len(numbers)}")
print(lower_letters[3:5])

print(f"random.choice(letters) = {random.choice(letters)}")


print(letters.index("A"))

new_numbers = numbers.copy()
new_numbers += '999'
print(new_numbers)

new_numbers = numbers.copy()
new_numbers.append('999')
print(new_numbers)

total = 0
for n in range(0,len(numbers)):
  total += int(numbers[n])
  print(f"total: {total}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(cards)
cards += [99]
print(cards)
for card in cards:
  print(card)

cards.append(86)
print(cards)

numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))