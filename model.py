

# customers
    # customer_id
    # name
    # password
    # address

# melon_types
    # melon_type_id
    # max_slices
    # name

# storage_spaces
    # storage_space_id
    # location
    # capacity

# melons
    # initial_slices
    # arrival_date
    # melon_type_id (fk)
    # storage_space_id (fk)

# orders
    # order_id
    # date
    # customer_id

# melon_orders
    # melon_order_id
    # melon_id (fk)
    # order_id (fk)