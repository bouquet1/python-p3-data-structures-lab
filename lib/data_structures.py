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
    food_names = []
    for food in spicy_foods:
        food_name = food["name"]
        food_names.append(food_name)
    return food_names


names_of_spicy_food = get_names(spicy_foods)
print(names_of_spicy_food)


# TASK: RETURNS A LIST OF DICTIONARIES the heat level of the food is > than 5.
def get_spiciest_foods(spicy_foods):
    spiciest_food_list = [
        food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food_list


print(get_spiciest_foods(spicy_foods))


# TASK: OUTPUT TO THE TERMINAL each spicy food in the following format using
# `print()`: `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")


print(print_spicy_foods(spicy_foods))


# TASK: returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


print(get_spicy_food_by_cuisine(spicy_foods, "American"))
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))


# TASK-5: OUTPUTS TO THE TERMINAL ONLY the spicy foods that have a heat level greater than 5, in the following format:
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_emoji = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
    # if food["heat_level"] > 9 denemesi yaptim
    # else:
    #     print("We don't have any food has heat_level more than 9")


print(print_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass
