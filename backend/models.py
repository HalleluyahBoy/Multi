# models.py

# admin
    # conversations
    # dashboards
    # history
    # marketplace
    # product_category
    # products_color
    # products_size
    # products_brand
    # products_rating
    # products_image
    # search
    # transactions
    # users
    # products
    # orders
    # category
    # buyer
    # seller
    # products
    # conversations
    # dashboards
    # senders
    # receivers
    # messages
    # timestamps
    # calls
    # trends
    # carts/Product_list
    # cartitem
    # order



# sorting and filtering
    # search
    # models.py
    # transactions
    # users
    # products
    # orders
    # category
    # buyer
    # seller
    # product





# marketplace
    # products
    # search
    # orders
    # category
    # buyer
    # seller
    # product


# transactions
    # users
    # products
    # orders
    # category
    # buyer
    # seller
    # product

# trends
    # users
    # products    
        # category
    # buyer
    # seller
    # product
        # orders
        # cart
        # cartitem
        # order
        # orderitem
        # shippingaddress
    # review
    # wishlists
        # wishlistitem
    # ratings


# product_category
# product_color
# product_size
# product_brand
# product_rating
# product_image


# conversations
    # sender
    # receiver
    # message
    # timestamp
    # call

# History
    # timestamp
    # sender
    # receiver
    # message
    # calls

# DashBoard
    # balance
    # transaction
    # orders
    # products
    # product




class Conversation:
    def __init__(self, sender, receiver, message, timestamp, call):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.timestamp = timestamp
        self.call = call



class Marketplace:
    def __init__(self):
        # Add your code here to initialize the Marketplace model
        pass

# class Admin:
#     def __init__(self):
#         # Add your code here to initialize the Admin model
#         pass

class Conversation:
    def __init__(self):
        # Add your code here to initialize the Conversation model
        pass

class SortingAndFiltering:
    def __init__(self):
        # Add your code here to initialize the SortingAndFiltering model
        pass
class Search:
    def __init__(self):
        # Add your code here to initialize the Search model
        pass


class Transactions:
    def __init__(self):
        # Add your code here to initialize the Transactions model
        pass

class History:
    def __init__(self):
        # Add your code here to initialize the History model
        pass

class DashBoard:
    def __init__(self, balance, transaction, order, product):
        self.balance = balance
        self.transaction = transaction
        self.order = order
        self.product = product


class ProductCategory:
    def __init__(self):
        # Add your code here to initialize the ProductCategory model
        pass

class ProductColor:
    def __init__(self):
        # Add your code here to initialize the ProductColor model
        pass

class ProductSize:
    def __init__(self):
        # Add your code here to initialize the ProductSize model
        pass

class ProductBrand:
    def __init__(self):
        # Add your code here to initialize the ProductBrand model
        pass

class ProductRating:
    def __init__(self):
        # Add your code here to initialize the ProductRating model
        pass

class ProductImage:
    def __init__(self):
        # Add your code here to initialize the ProductImage model
        pass