
PRICE_UNIT = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 10
}

SPECIAL_OFFERS = {
    'A': {
        'number': 3,
        'price': 130
    },
    'B': {
        'number': 2,
        'price': 45
    }
}


def deserialize(skus):
    return skus.replace(' ', '').split(',')


def calculate_price(item_type, number):



# noinspection PyUnusedLocal
def checkout(skus):
    # Let's assume that the skus format is "A, B, C, A, D"
    # Let's also assume that a special offer can be applied multiple times, i.e. "3A for 130" makes 6A cost 260

    # First extract the skus in a more proper structure to deal with
    # If I'm wrong with the assumed format, this will be the only step to be changed.
    product_list = deserialize(skus)

    # Count the number of items per product
    items_counter = {i:product_list.count(i) for i in product_list}

    # For each product, count the total price
    total_price = 0

    for item, number in items_counter:
        item_total_price = calculate_price(item, number)

    # Sum the total of each product

    raise NotImplementedError()
