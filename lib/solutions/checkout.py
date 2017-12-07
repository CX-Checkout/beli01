

PRICE_UNIT = {
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
    'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
    'Y': 20, 'Z': 21
}


SAME_PRODUCT_OFFERS = {
    'A': [{
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
    'B': [{
        'number': 2,
        'price': 45,
        'priority': 1
    }],
    'H': [{
            'number': 10,
            'price': 80,
            'priority': 1
        },
        {
            'number': 5,
            'price': 45,
            'priority': 2
        }
    ],
    'K': [{
        'number': 2,
        'price': 150,
        'priority': 1
    }],
    'P': [{
        'number': 5,
        'price': 200,
        'priority': 1
    }],
    'Q': [{
        'number': 3,
        'price': 80,
        'priority': 1
    }],
    'V': [{
            'number': 3,
            'price': 130,
            'priority': 1
        },
        {
            'number': 2,
            'price': 90,
            'priority': 2
        }
    ]
}


INTER_PRODUCT_OFFERS = {
    'E': {
        'number': 2,
        'target': 'B',
        'price': 0
    },
    'F': {
        'number': 3,
        'target': 'F',
        'price': 0
    },
    'N': {
        'number': 3,
        'target': 'M',
        'price': 0
    },
    'R': {
        'number': 3,
        'target': 'Q',
        'price': 0
    },
    'U': {
        'number': 4,
        'target': 'U',
        'price': 0
    }
}


INTER_PRODUCT_MIX = [{
    'products': ['S', 'T', 'X', 'Y', 'Z'],
    'price': 45
}]


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

    return skus


def calculate_price(item_type, number):
    print('Calculate price for {}'.format(item_type))
    # First check if there is a special offer.
    if item_type not in SAME_PRODUCT_OFFERS.keys():
        no_discount_price = PRICE_UNIT[item_type] * number
        print('Price for {}: {}'.format(item_type, no_discount_price))
        return no_discount_price

    # Now we know that's a special offer, we should know how many items are affected by the promotions
    offer_information = SAME_PRODUCT_OFFERS[item_type]
    sorted_offers = sorted(offer_information, key=lambda x: x['priority'])
    print(sorted_offers)
    item_total_price = 0
    remaining_product_number = number

    for offer_information in sorted_offers:

        # Check the number of special offers per product
        number_of_offers = remaining_product_number / offer_information['number']

        # Get the number of affected products
        affected_product_number = number_of_offers * offer_information['number']
        remaining_product_number -= affected_product_number

        item_total_price += number_of_offers * offer_information['price']

    # Check the number of products not usable by any special offer
    item_total_price += remaining_product_number * PRICE_UNIT[item_type]
    print('Price for {}: {}'.format(item_type, item_total_price))

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

    if not product_list:
        return 0

    # Count the number of items per product, and associated price
    items_counter = {i: {'count': product_list.count(i), 'price': 0} for i in product_list}
    print(items_counter)
    # Fill missing counts
    for item_type in PRICE_UNIT.keys():
        if item_type not in items_counter.keys():
            items_counter.update({item_type: {'count': 0, 'price': 0}})

    total_price = 0

    for item_type, offer in INTER_PRODUCT_OFFERS.items():
        offer_nb = items_counter[item_type]['count'] / offer['number']
        target_item_type = offer['target']
        if offer['price'] == 0:
            nb_remaining_items = items_counter[target_item_type]['count'] - offer_nb
            if nb_remaining_items < 0:
                nb_remaining_items = 0
            items_counter[target_item_type]['count'] = nb_remaining_items

    for item, information in items_counter.items():
        # For each product, count the total price
        # And add it to the total of each product

        total_price += calculate_price(item, information['count'])




    return total_price
