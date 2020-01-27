import random
from acme import Product

ADJETIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products = 30):
    products = []
    for _ in range(num_products):
        name = random.sample(ADJETIVES, 1)[0] + " " + random.sample(NOUNS, 1)[0]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        products.append(Product(name = name, price = price,
                                weight = weight, flammability = flammability ))
    return products

def inventory_report(products):
    names, prices, weights, flammabilities = [], [], [], []
    for x in range(len(products)):
        names.append(products[x].name)
        prices.append(products[x].price)
        weights.append(products[x].weight)
        flammabilities.append(products[x].flammability)
    
    Unique_prod_names = len(set(names))
    
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Product name:' , Unique_prod_names)
    print('Average price:' , sum(prices)/len(prices))
    print('Average weight:' , sum(weights)/len(weights))
    print('Average flammability:' , sum(flammabilities)/len(flammabilities))
    pass
    
if __name__ == '__main__':
    inventory_report(generate_products())