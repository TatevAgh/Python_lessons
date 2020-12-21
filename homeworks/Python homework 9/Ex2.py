# *Create a class for representing shop with some attributes (employees names,
# products names and prices, income, owner) and behavior (add employee, remove employee,
# add products, find product by name, find products cheaper than some specific value,
# change owner, increase income), create several shops and perform operations on them

class Shop:
    def __init__(self, employees, products_and_prices, income, owner):
        self.employees = employees
        self.products_and_prices = products_and_prices
        self.income = income
        self.owner = owner

    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        return self.employees

    def del_employee(self, del_employee):
        self.employees.remove(del_employee)
        return self.employees

    def add_products(self, new_product, new_price):
        self.products_and_prices[new_product] = new_price
        return self.products_and_prices

    def find_prod_by_name(self, product_name):
        del self.products_and_prices[product_name]
        return self.products_and_prices

    def find_cheaper_than(self, cheaper_than_value):
        return dict(filter(lambda value: cheaper_than_value > value[1], self.products_and_prices.items()))

    def change_owner(self, new_owner):
        self.owner = new_owner
        return self.owner

    def increase_income(self, increase_value):
        self.income *= increase_value
        return self.income


candy_employees = ['Gregory', 'Sergey', 'Anahit', 'John']
candy_products_and_prices = {'Sweets Candies': 5, 'Soft Drink': 3, 'Mineral Water': 2, 'Home Made Fudge': 6, 'Imported Candy': 3}
candy_income = 500
candy_owner = 'Curtis James Jackson'
candy_shop = Shop(candy_employees, candy_products_and_prices, candy_income, candy_owner)
pet_employees = ['Anny', 'Mary', 'Joanna', 'Will']
pet_products_and_prices = {'Dry Dog Food': 10, 'Dog Treats & Dog Bones': 15, 'Dog Toys': 7, 'Dog Clothing': 9, 'Special Food': 4}
pet_income = 650
pet_owner = 'Judy Anderson'
pet_shop = Shop(pet_employees, pet_products_and_prices, pet_income, pet_owner)

print('Adding employee: ', candy_shop.add_employee('Garegin'))
print('Delete employee in shop', candy_shop.del_employee('John'))
print('Adding product to our products: ', candy_shop.add_products('Sugar Free Candy', 5))
print('Finded product by name: ', candy_shop.find_prod_by_name('Soft Drink'))
print('Product cheaper than 5 :', candy_shop.find_cheaper_than(5))
print('New Owner of the Candy shop is: ', candy_shop.change_owner('Calvin Cordozar Broadus'))
print('Increased income of the Candy shop is: ', candy_shop.increase_income(2))

print('Adding employee: ', pet_shop.add_employee('Betty'))
print('Delete employee in shop', pet_shop.del_employee('Joanna'))
print('Adding product to our products: ', pet_shop.add_products('Dog Clothing', 9))
print('Finded product by name: ', pet_shop.find_prod_by_name('Dog Toys'))
print('Product cheaper than 5 :', pet_shop.find_cheaper_than(9))
print('New Owner of the Pet shop is: ', pet_shop.change_owner('Henry Tomson'))
print('Increased income of the Pet shop is: ', pet_shop.increase_income(3))