dic ={
			"Blueberry":    {"price": 1.00, "stock": 10},
			"Canberry" :    {"price": 1.50, "stock": 10},
			"Kiwi"     :    {"price": 2.00, "stock": 10},
			"Orange"   :    {"price": 1.20, "stock": 10}
		}
print('Looping through all the items of the outer dictionary:')
for fruit,info in dic.items():
	print(f"FRUIT: {fruit}")
	for key,value in info.items():
		print(f"{key.capitalize()}: {value}")


new_dic = {"orange": 1.20,
		   "apple": 9.20,
		   "mandarin": 2.30}

print()
print('-------------------------------------------------')
print('Removing and replacing a key:')
new_dic["lemon"] = new_dic.pop ("orange")
print(new_dic)

print()
print('Assigning new value to a key:')
new_dic ["apple"] = 0.00
print(new_dic)

print()
print('-------------------------------------------------')

'''
#MOVIE TICKETS DICTIONARY
print("------------------------------------------------")
print("MOVIE TICKETS")

ticket_types = {
	'Standard':  {'price': 5.99, 'stock':10},
	'Luxury':    {'price':9.99, 'stock':8},
	'Premium':   {'price':15.99, 'stock':5}

}

def fill_cart(Standard,Luxury,Premium):
	cart = {
		'Standard': Standard,
		'Luxury'  : Luxury,
		'Premium' : Premium
	}
	print()

	print('YOUR CART')
	for item,qty in cart.items():
		if item in ticket_types:
			price = ticket_types[item]['price']
			total_price = price * qty
			print(f"{item}: {qty} unit(s) x ${price:.2f} = ${total_price:.2f}")
	print()
	return cart
	#When the function is done running, cart is return which is a dictionary.

def calculate_total_price(fill_cart):
	total_price = 0
	for ticket,qty in cart.items():
			ticket_price = ticket_types[ticket]['price']
			total_price += ticket_price * qty
	print(f'TOTAL PRICE: ${total_price}')
	return total_price

def update_inventare(cart):
	for item,qty in cart.items():
		if item in ticket_types:
			ticket_types[item]['stock'] -= qty
			print(f' Ticket:{item}    Available in stock: {ticket_types[item]['stock']}')


#The 'cart' dictionary is stored in the instance cart.
#The 'cart' instance is used when calling the second function.
cart = fill_cart(2,1,5)
cart = calculate_total_price(cart)
'''

'''
print()
print("------------------------------------------------")
print("ICE CREAM")

ice_creams = {
	"Chocolate" : {'price': 2.30, 'calories': 345},
	"Pistachio" : {'price': 7.20, 'calories': 399},
	'Blueberry' : {'price': 5.60, 'calories': 240}
}

ice_cream2 = {
	"Chocolate" : 2.30,
	"Pistachio" : 7.20,
	'Blueberry' : 5.60
}

portion1 = list(ice_cream2.values())
print(portion1)

portion2 = ice_creams['Blueberry']['calories']
print(portion2)

print('---------------------------------------------------------------------------------')
print("Accessing all items of the inner dictionary of the 'Blueberry' ice cream flavour")
print(ice_creams['Blueberry'].items())
print()
print("Accessing all keys of the inner dictionary of the 'Blueberry' ice cream flavour")
print(ice_creams['Blueberry'].keys())
print()
print("Accessing all values of the inner dictionary of the 'Blueberry' ice cream flavour")
print(ice_creams['Blueberry'].values())
print()

print("-------------------------------------------------------------------------------------")
print('Looping though the inner dictionary values:')
for info in ice_creams.values():
	price = info['price']
	calories = info['calories']
	print(f'Price: {price}, Calories: {calories}')

print()
print("---------------------------------------------------------------------------------------")
print("Looping through the inner one value")
for flavour,info in ice_creams.items():
	calories = info['calories']
	print(f'Ice cream: {flavour} Calories: {calories}')

print()
print("---------------------------------------------------------------------------------------")
print("Looping through the inner one value")
for ice_cream,ice_info in ice_creams.items():
	pric = ice_info['price']
	calorie = ice_info['calories']
	print(f"Ice cream --> {ice_cream} \nPrice: {pric} \nCalories: {calorie}")
'''
print()
print("------------------------------------------------")
print("LIP GLOSS")

lipgloss = {
	'Red' : {'price': 7.88, 'stock':10},
	'Pink': {'price': 18.80, 'stock':10},
	'Purple': {'price': 7.99, 'stock':10}
}

def fill_basket(red,pink,purple):
	basket = {
		'Red': red,
		'Pink': pink,
		'Purple': purple
	}
	return basket

def to_price_cal(basket):
	total_price = 0
	for item,quantity in basket.items():
		lipgloss_price = lipgloss[item]['price']
		total_price += lipgloss_price * quantity
	print(f'TOTAL PRICE: ${total_price}')
	return total_price
def update_in(basket):
    for item, qty in basket.items():
        lipgloss[item]['stock'] -= qty
        print(f"Product: {item} | Stock: {lipgloss[item]['stock']}")

cus1 = fill_basket(5,8,2)
to_price_cal(cus1)
update_in(cus1)