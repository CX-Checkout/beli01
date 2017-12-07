

PRICE_UNIT = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


SAME_PRODUCT_OFFERS = {
    'A': [
        {
            'number': 5,
            'price': 200,
            'priority': 1
        },
        {
            'number': 3,
            'price': 130,
            'priority': 2
        }
    ],
    'B': {
        'number': 2,
        'price': 45
    }
}


INTER_PRODUCT_OFFERS = {
    'E': {
        'number': 2,
        'target': 'B',
        'price': 0
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
    if item_type not in SAME_PRODUCT_OFFERS.keys():
        return PRICE_UNIT[item_type] * number

    # Now we know that's a special offer, we should know how many items are affected by the promotions
    offer_information = SAME_PRODUCT_OFFERS[item_type]
    sorted_offers = sorted(offer_information, key=lambda x: x['priority'])

    item_total_price = 0
    remaining_product_number = number

    for special_offer in sorted_offers:

        # Check the number of special offers per product
        number_of_offers = number / offer_information['number']

        # Get the number of affected products
        affected_product_number = number_of_offers * offer_information['number']
        remaining_product_number -= affected_product_number

        item_total_price += number_of_offers * offer_information['price']

    # Check the number of products not usable by any special offer
    item_total_price += remaining_product_number * PRICE_UNIT[item_type]

    return item_total_price


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

    for item_type, offer in INTER_PRODUCT_OFFERS.items():
        offer_nb = items_counter[item_type] / offer['number']
        target_item_type = offer['target']
        if offer['price'] == 0:
            nb_remaining_items = items_counter[target_item_type] - offer_nb
            if nb_remaining_items < 0:
                nb_remaining_items = 0
            items_counter[target_item_type] = nb_remaining_items

    for item, number in items_counter.items():
        # For each product, count the total price
        # And add it to the total of each product

        total_price += calculate_price(item, number)

    return total_price
