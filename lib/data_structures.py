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

# RETURNS A LIST OF STRINGS with the names of each spicy food


def get_names(spicy_foods):
    food_names = []   # Create an empty list to store the names
    for food in spicy_foods:
        food_name = food["name"]
        food_names.append(food_name)  # Add the name to the list
    return food_names


names_of_spicy_food = get_names(spicy_foods)
print(names_of_spicy_food)
# output => ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']


# RETURNS A LIST OF DICTIONARIES where the heat level of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    # list comprehension to filter out the foods' heat level > 5
    spiciest_food_list = [
        food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food_list


print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass


def print_spiciest_foods(spicy_foods):
    pass


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass
