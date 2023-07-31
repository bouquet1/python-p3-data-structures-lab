spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# TASK: RETURNS A LIST OF STRINGS with the names of each spicy food


def get_names(spicy_foods):
    food_names = []   # Create an empty list to store the names
    for food in spicy_foods:
        food_name = food["name"]
        food_names.append(food_name)  # Add the name to the list
    return food_names


names_of_spicy_food = get_names(spicy_foods)
print(names_of_spicy_food)
# output => ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']


# TASK: RETURNS A LIST OF DICTIONARIES where the heat level of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    # list comprehension to filter out the foods' heat level > 5
    spiciest_food_list = [
        food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food_list


print(get_spiciest_foods(spicy_foods))
# output => [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]


# TASK: OUTPUT TO THE TERMINAL each spicy food in the following format using
# `print()`: `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.
def print_spicy_foods(spicy_foods):
    # for loop to iterate through each food.
    # each iteration, the variable 'food' will hold the current dictionary that represents a spicy food with information name, cuisine, heat level.
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        # Repeat the chili emoji based on the heat level
        heat_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")


print(print_spicy_foods(spicy_foods))
# output => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
# None (like undefined in JS becasue we didn't return a value we just printed a string)


# TASK: function takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


print(get_spicy_food_by_cuisine(spicy_foods, "American"))
# output => {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
# output => {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}


def print_spiciest_foods(spicy_foods):
    pass


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass
