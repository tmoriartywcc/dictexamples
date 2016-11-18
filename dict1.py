products = {}

prod_id = int(input("please enter prod id (-99) to stop"))
prod_name = ""
while prod_id != -99:
    prod_name = input("please enter prod name")
    products[prod_id] = prod_name
    prod_id = int(input("please enter prod id (-99) to stop"))

print(len(products))
print(products)

prod_id = int(input("please enter product to look up"))

if prod_id in products:
    print(products[prod_id])
else:
    print("Product ID", prod_id, "not in dict")

#new_prod_id = int(input("Enter new int prod id"))
#new_prod_name = input("Enter new prod name")

#products[new_prod_id] = new_prod_name

