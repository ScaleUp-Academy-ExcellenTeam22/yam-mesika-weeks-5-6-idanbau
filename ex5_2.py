def join(*lists: list, seperator: str = '-'):
    """
    A function that receive unlimited lists and combine them with seperator between each other.
    :param lists: Unlimited list to combine
    :param seperator: Seperator between each list
    :return: Return the list with seperator in the end (without the last character)
    """
    return [list_cell for curr_list in lists for list_cell in curr_list + [seperator]][:-1]


def get_recipe_price(ingredients_prices: dict, optionals: list = (), **ingredients_quantity: int):
    """
    This function get ingredients, optionals ingrediants and their quantity
    on grams and returns the price to cook the recipe
    :param ingredients_prices: Map of ingredients and their prices for 100 grams
    :param optionals: List of optional ingredients from the list which will not be calculated
    :param ingredients_quantity: The quantitiy by grams needed for each ingredient in order to cook the recipe
    :return: The total price to cook the specific recipe
    """
    return sum(ingredients_quantity[key] / 100 * ingredients_prices[key]
               for key in ingredients_prices.keys() if key not in optionals)

