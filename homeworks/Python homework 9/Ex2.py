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
