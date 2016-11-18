products = {123:"hammer", 234:"wrench", 555:"saw"}


#for key in products:
#    print(products[key])

prod_id = int(input("enter product id"))

#print(products.get(prod_id, "NOT FOUND"))
print(products)

print(products.pop(prod_id, str(prod_id) + 'not found'))

print(products)
