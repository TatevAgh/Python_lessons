# *Define collection of prices, calculate their sum until meeting negative price
prices = [45, 5, -4, 4, 0]
sum = 0
for price in prices:
    if price < 0:
        break
    else:
        sum += price
print('their sum until meeting negative price', sum)