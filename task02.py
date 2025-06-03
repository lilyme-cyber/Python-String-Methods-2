product = input("Mahsulotni kiriting: ")
cost = input("Narxni kiriting: ")

template = "{product} mahsuloti narxi  ${cost}!"

result = template.format(product=product, cost=cost)

print("Natija", result)
