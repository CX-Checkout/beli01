

PRICE_UNIT = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
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


class IllegalInput(Exception):
    pass


def deserialize(skus):
    if not skus:
        return []

    skus_list = []

    # Split different products
    skus = skus.replace(' ', '')

    # Check if they are in the allowed values
    for sku in skus:
        if sku not in PRICE_UNIT.keys():
            raise IllegalInput('Product not recognised')
        skus_list.append(sku)

    return skus


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
    try:
        product_list = deserialize(skus)
    except IllegalInput:
        return -1

    # Count the number of items per product
    items_counter = {i:product_list.count(i) for i in product_list}

    total_price = 0

    for item, number in items_counter.items():
        # For each product, count the total price
        # And add it to the total of each product
        total_price += calculate_price(item, number)

    return total_price
