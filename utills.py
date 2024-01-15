from src.database.connection import DatabaseManager
from src.controller.people import create_person, read_people, update_person, delete_person
from src.controller.product import create_product, read_products, update_product, delete_product
from src.controller.sell import create_sell, read_sells, update_sell, delete_sell

#create_person('Josias', '51997613120', '13593464730')

#people = read_people()
#for person in people:
#    print(person.name)

#person = update_people(1, 'Pedro Henrique')
#print(person)

#delete_person(1)

#-----

#create_product('Água', 5.99, '5555', 2)

#products = read_products()
#for product in products:
#    print(product.name)

#update_product(1, 'Carvão')

#delete_product(1)

#-----

create_sell(2, 1, 3, 15.99)