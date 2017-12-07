def deserialize(skus):
    return skus.replace(' ', '').split(',')


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

    # Sum the total of each product

    raise NotImplementedError()
