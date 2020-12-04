# Create a collection of company names, generate a collection of company names ending with ‘s’ (create a function),
# generate a collection of company names containing different symbols combination by default double ‘o’ (create a function), print results

collection_companies = ['Apple', 'Microsofts', 'Walmart', 'Amazon', 'Volkswagen', 'Facebooks', 'Nestlé', 'Google', 'Walgreens', 'Glencore', 'Sinopec']

def ending_with_s(companies):
    """Returns names that ends with s """
    names_s = []
    for company in companies:
        if company.lower()[-1] == 's':
            names_s.append(company)
    return names_s

def names_with_combination(companies, combination):
    """"Searches the name of company that contains some combination"""
    for company in companies:
        if combination in company:
            print(company)

names_with_combination('Companies that have some comobination', collection_companies, 'oo')
names_with_combination('Companies that have some comobination', collection_companies, 'pp')
names_with_combination('Companies that have some comobination', collection_companies, 'ee')
print('Names ending with s', ending_with_s(collection_companies))