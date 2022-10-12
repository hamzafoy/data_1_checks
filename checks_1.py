# Basic Hello World statement printed
print("Hello World!")

# Build a List using user input, print one to the terminal.
print("Enter three country names of your choice!")
user_provided_values = [input(), input(), input()]
print(user_provided_values[1], "is the second country you submitted!")

# Build a dictionary of three-country lists using user's previous input & a predetermined from computer.
countries = {'user': user_provided_values, 'comp': ['Italy', 'Mozambique', 'Pakistan']}
print(countries[input("Type 'user' to see countries you listed, 'comp' to see the computers' preferred country ")])

# Build a tuple and print on of the values.
example_tuple = (12.6667, 10260, "Aragorn", [1,2,3])
print(example_tuple[3])