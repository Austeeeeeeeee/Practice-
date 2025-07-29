import random
''''
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



'''
#MOVIE TICKETS DICTIONARY
print("--------------- MOVIE TICKETS ---------------")

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
print("--------------- ICE CREAM ---------------")
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


'''
print()
print("--------------- LIP GLOSS ---------------")

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

def calculate_basket_price(basket):
	total_price_item = 0
	total_price = 0
	for item, qty in basket.items():
		lip_price = lipgloss[item]['price']
		total_price_item = lip_price * qty
		print(f'ITEM: {item} - {qty} unit(s) x ${lip_price} = {total_price_item}')
		total_price += lip_price * qty
	print(f'TOTAL TO PAY: {total_price}')
	print()

def update_inventary(basket):
	for item,qty in basket.items():
		lipgloss[item]['stock'] -= qty
		print(f'Item: {item} Stock left: {lipgloss[item].get('stock')}')



cus1 = fill_basket(5,8,2)
calculate_basket_price(cus1)
update_inventary(cus1)

'''


print()
print("------------------------------------------------")
print("CAKE STORE")

def welcoming_message():
	print('Hello! Welcome to CAKELAND!')
def cake_flavours_function():
	cake_flavours = {
		'Chocolate': {'base_price': 20.25, 'stock': 5},
		'Vanilla': {'base_price': 15.80, 'stock': 5},
		'Strawberry': {'base_price': 5.75, 'stock':5}
	}
	return cake_flavours
def cake_size():
	cake_sizes = {
		'Small': 5,
		'Medium': 10,
		'Large': 8}
	return cake_sizes

def fi_cart():
	cart = {}
	cake_options = cake_flavours_function()
	print('--------------- SELECT YOUR FLAVOUR --------------- ')
	while True:
		print(f'OPTIONS: {list(cake_options.keys())}')
		print('-- Enter your flavour: ')
		computer_choice = random.choice(list(cake_options.keys()))
		print(f'-- {computer_choice}')

		if computer_choice in cake_options:
				max_stock = cake_options[computer_choice]['stock']
				valid_quantities = list(range(0,max_stock,+ 1))
				computer_choice_quantity = random.choice(valid_quantities)

				print('--------------- SELECT YOUR AMOUNT --------------- ')
				print(f' -- How many {computer_choice} cakes do you want? ')
				cart[computer_choice] = computer_choice_quantity
				print(f'-- {computer_choice_quantity}')

				print('--------------- SELECT YOUR SIZE --------------- ')
				cake_siz = cake_size()
				print(f'OPTIONS: {list(cake_siz.keys())}')
				computer_choice_size = random.choice(list(cake_siz.keys()))
				print(f'-- {computer_choice_size}')
				print()


				valid_options = ['Yes','No']
				computer_choice_yesno = random.choice(valid_options)
				print('-- Do you want to add another flavour? (yes/no): ')
				new_computer_choice = computer_choice_yesno.capitalize()
				if new_computer_choice == 'Yes':
					continue
				elif new_computer_choice == 'No':
					print(new_computer_choice)
					print('Gotta! Thanks for you order. Now printing your basket!')
					break
	return cart


def print_cart(cart,cake_flavours):
	print('--------------- YOUR BASKET ---------------')
	total_price = 0
	for item,quantity in cart.items():
			base_price_cake = cake_flavours[item]['base_price']
			total_price_per_cake = base_price_cake * quantity
			print(f"ITEM: {item} | Quantity: {quantity} x {base_price_cake} | Total per cake: {total_price_per_cake} EUR")
			total_price += base_price_cake * quantity
	print(F'TOTAL TO PAY: {total_price} EUR')

def update_inventory(cart,cake_flavours):
		print('-------- STOCK CHOSEN --------------------')
		for i,q in cart.items():
			cake_flavours[i]['stock'] -= q
		print(f'ITEM: {i} STOCK: {cake_flavours[i]['stock']}')
		print()

		print('---------- UPDATED STOCK -----------------')
		for name,details in cake_flavours.items():
			print(f'NAME: {name} -- STOCK: {details['stock']}')




cartt = fi_cart()
c_f = cake_flavours_function()
print_cart(cartt,c_f)
update_inventory(fi_cart(),cake_flavours_function())



'''
print()
print("-------------------------------------------------------------------------------------")
print('Practice how to access nested dictionaries:')
print('Method 1: Unpacking using a loop for multiple keys and values')

nested_dictionary = {
	'Yellow' : {'price': 1, 'stock': 9},
	'Purple' : {'price': 23, 'stock': 22},
	'Green' : {'price': 16, 'stock': 15},
}

for color, details in nested_dictionary.items():
	price = details['price']
	stock = details['stock']
	print(f'{color} --> {price} --> {stock}')

print()
print('Method 2: Unpacking using a loop for multiple keys and values (shorther way)')
for color,detail in nested_dictionary.items():
	price,stock = detail['price'],detail['stock']
	print(f'{color} --> {price} --> {stock}')


print()
print('Method 3: Assigning variables to store nested keys and values')
price = nested_dictionary.values()
color = nested_dictionary.keys()
print(list(price))
print(list(color))

print()
print('--------------------------------------------------------------')
print('Access the values of the inner dictionary')
for detail in nested_dictionary.values():
	for value in detail.values():
		if value == 1:
			print(value)


for detail in nested_dictionary.values():
	for key, value in detail.items():
		if value == 1:
			print(f"{key}: {value}")
'''