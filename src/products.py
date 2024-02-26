from modells import Product

def create_product(name, value, quantity):
    product = Product
    product.name = name
    product.value = value
    product.quantity = quantity
    return product