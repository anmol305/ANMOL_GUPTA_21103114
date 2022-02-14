numbers = (input("Enter the numbers with ',' between them :- ")).split(",")

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

my_dictionary = {}
for i in numbers:
    my_dictionary[i] = i ** 2

tups = my_dictionary.items()
print(tups)