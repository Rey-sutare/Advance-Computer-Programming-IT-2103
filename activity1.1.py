name = input('Enter your Name:')
age = int(input('Enter your Name:'))
address=input('Enter your Address:')

print("Information Received")
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Address:{address}")


# Output: 79 (sum)
a = 7
b = 9
sum_result = a + b
print(f"Output: {sum_result} (sum)")

# a=7, product = 5*a, what would be the output?
a = 7
product = 5 * a
print(f"a = {a}, product = {product}, what would be the output?")

# a=2, b = 11, a = a* 2, b = b+(c *3), c = a *b, what would be the output?
a = 2
b = 11
c = 0
a = a * 2
b = b + (c * 3)
c = a * b
print(f"a = {a}, b = {b}, c = {c}, what would be the output?")

# The user can input two numbers, display the sum of the two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_input = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_input}")

# Squared = 3**2, cubed = 3**3, what would be the output?
squared = 3**2
cubed = 3**3
print(f"Squared: {squared}, Cubed: {cubed}")

# Name = "Gly", output would be Your name is Gly
Name = "Gly"
print(f"Your name is {Name}")

# True or False. Apple_price = 20, orange_price = 20.
Apple_price = 20
orange_price = 20
print(f"True or False. Apple_price = orange_price: {Apple_price == orange_price}")
