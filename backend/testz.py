# models.py



# Core models

class login:
    # fields for login
    class Signup:
        # fields for signup
        pass
    class User:
        # fields for user
        pass
    if User == Signup:
        pass
    pass

class User:
    # fields for user
    # User IDS
        # Phone number
        # Email
        Phone_number = ""
        Email = ""
        Password = ""
        account_type = ""
        # User profile
        name = ""
        passport_number = ""
        date_of_birth = ""
        gender = ""
        account_details = ""
        wallet_address = ""

        # User address
        address = ""
        city = ""
        state = ""
        pincode = ""
        country = ""

        # User status
        online = ""
        online_status = ""
        # User settings
        notification = ""
        notification_status = ""
        # User profile picture
        profile_picture = ""
        # User profile banner
        profile_banner = ""
        # User profile description
        profile_description = ""
    # relationships: login, product, order, transaction, conversation, message, call
   
class Category:
    # fields for category
    pass

class Product:
    # fields for product
    # relationships: category, seller, buyer, product_image, product_color, product_size, product_brand, product_rating
    pass

class Order:
    # fields for order
    # relationships: user, product, order_item, shipping_address
    # Place order
    class place_order:
        # fields for place order
        pass
    # payment
    class payment:
        # fields for payment
        pass
    # cancel order
    # order status
    class cart:
        # fields for cart
        pass
    class cart_item:
        # fields for cart item
        pass
    class order_item:
        # fields for order item
        pass
    class shipping_address:
        # fields for shipping address
        pass
    # relationships: user (buyer), user (seller), product, transactions

    class Cart:
        # fields for cart
        # relationships: user, cart item
        pass

    class CartItem:
        # fields for cart item
        # relationships: cart, product
        pass







# Product-related models
class ProductCategory:
    # fields for product category  
    class ProductColor:
        # fields for product color
        pass

    class ProductSize:
        # fields for product size
        pass

    class ProductBrand:
        # fields for product brand
        pass

    class ProductRating:
        # fields for product rating
        pass

    class ProductImage:
        # fields for product image
        pass







# Transactions-related models
class Transaction:
    # fields for transaction
    # relationships: user, product, order
    pass

# Conversations-related models
class Conversation:
    # fields for conversation
    pass

class Message:
    # fields for message
    # relationships: sender, receiver, timestamp
    pass

class Call:
    # fields for call
    # relationships: sender, receiver, timestamp
    pass






# DashBoard-related models
class Dashboard:
    # fields for dashboard
    # relationships: user, transaction, order, product
    pass



# Sorting and Filtering
class Search:
    # fields for search
    pass

# Trends-related models
class Trend:
    # fields for trend
    # relationships: user, product, order, cart, cart item, order item, shipping address, review, wishlist item, rating
    pass



# History-related models
class History:
    # fields for history
    # relationships: timestamp, sender, receiver, message, call
    pass

# Additional models
class Wishlist:
    # fields for wishlist
    # relationships: user, wishlist item
    pass

class WishlistItem:
    # fields for wishlist item
    # relationships: product
    pass

class Review:
    # fields for review
    # relationships: user, product
    pass

# Carts-related models


class ShippingAddress:
    # fields for shipping address
    # relationships: user, order
    pass
