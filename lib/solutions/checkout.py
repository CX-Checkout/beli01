

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
    # First check if there is a special offer.
    if item_type not in SPECIAL_OFFERS.keys():
        return PRICE_UNIT[item_type] * number

    # Now we know that's a special offer, we should know how many items are affected by the promotions
    offer_information = SPECIAL_OFFERS[item_type]

    # Check the number of special offers per product
    number_of_offers = number / offer_information['number']

    # Check the number of products not usable by the special offer
    left_over_products = number % offer_information['number']

    return number_of_offers * offer_information['price'] + left_over_products * PRICE_UNIT[item_type]


# noinspection PyUnusedLocal
def checkout(skus):
    # Let's assume that the skus format is "A, B, C, A, D"
    # Let's also assume that a special offer can be applied multiple times, i.e. "3A for 130" makes 6A cost 260

    # First extract the skus in a more proper structure to deal with
    # If I'm wrong with the assumed format, this will be the only step to be changed.
    product_list = deserialize(skus)

    # Count the number of items per product
    items_counter = {i:product_list.count(i) for i in product_list}

    total_price = 0

    for item, number in items_counter:
        # For each product, count the total price
        # And add it to the total of each product
        total_price += calculate_price(item, number)

    return total_price
