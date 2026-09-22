# Personal Information Manager
# My first Python project

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Siva Prakash V"
degree = "B.Tech. Artificial Intelligence and Data Science"
age = 21
city = "Chennai"
hobby = "playing Volleyball"
Interests = ["AI", "Data Science", "Machine Learning", "Deep Learning"]

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_car = input("What's your favorite car? ")
while favorite_car == "":
    print("Please enter a valid car!")
    favorite_car = input("What's your favorite car? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"degree: {degree}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Interests: {Interests}")
print()
print(f"Favorite car: {favorite_car}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)