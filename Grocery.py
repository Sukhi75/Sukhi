def fileToDictionary(filename):
    d = {}

    for line in filename:
        data = line.split()
        key, value = data[0], data[1]
        d[key] = float(value)
    print(d)
    return d


def billBasket(basket, products):

    total =0
    basketdict = fileToDictionary(basket)
    productsdict = fileToDictionary(products)
    #to calculate total
    for productname, qty in basketdict.items():
        total = total + productsdict.get(productname)* qty

    return total

try:
    basket = open("basket.txt")
    products = open("products.txt")
    print("Total bill is =",billBasket(basket, products))

except FileNotFoundError:
    print("File not found, please check the file name or directory")
except NameError:
    print("File doesnt exist")
except Exception:
    print("Error occured, please check input ")