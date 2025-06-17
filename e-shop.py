class Fruitshop():
	def __init__(self,name='Juicy_niam',inventory=None,cart=None,discount=0,shipping_threshold=20.0,shipping_cost=4.99):
		self.name = name
		self.inventory = inventory if inventory is not None else {
			"Computer"   :    {"price": 500, "stock": 5},
			"Headphone" :     {"price": 57, "stock": 10},
			"USB_cable"  :    {"price": 13.50, "stock": 15},
			"Mouse"      :    {"price": 9.00, "stock": 20}
		}
		self.cart = cart if cart is not None else {}

		self.discount = discount
		self.shipping_threshold = shipping_threshold
		self.shipping_cost = shipping_cost


	def valid_user_input(self,product,valid_range):
		while True:
			user_input = int(input(f'How many {product} do you want? {valid_range}'))
			if user_input not in valid_range:
				print('Not enough stock!')
			else:
				print('Order placed!')
				return user_input

	def fill_cart(self, computer_range=None):
		print('Select the items you want:')
		if computer_range is None:
			stock = self.inventory['Computer']['stock']
			computer_range = list(range(1, stock + 1))
		self.cart['Computer'] = self.valid_user_input('computers',computer_range)

	def display_cart(self):
		print('YOUR CART:')
		for item, qty in self.cart.items():
			if item in self.inventory:
				price = self.inventory[item]['price']
				total = price * qty
				print(f"{item}: {qty} unit(s) x ${price:.2f} = ${total:.2f}")
		print('------------------------------------------------------------')
		print()

	def show_updated_inventory(self):
		print("UPDATED INVENTORY")
		for item,qty in self.cart.items():
				self.inventory[item]['stock'] -= qty
				print(f'{item}:{self.inventory[item]['stock']} left in stock')
	print()

	def price_calculation(self):
		print('PRICE TO PAY:')
		self.total_to_pay = 0
		for item, qty in self.cart.items():
			price = self.inventory[item]['price']
			self.total_to_pay += price * qty
		print(f"Total price: ${self.total_to_pay:.2f}")
		return self.total_to_pay


	def check_discount(self):
		if self.total_to_pay < 100:
			print('Sorry, no discount!')
		elif 100 <= self.total_to_pay <= 500:
			print('You get 5% discount!')
			self.discounted_price = self.total_to_pay * 0.95
			print(f'Discounted price: {self.discounted_price:.2f}')
			return self.discounted_price
		elif 500 < self.total_to_pay <= 800:
			print('You get 10% discount!')
			self.discounted_price = self.total_to_pay * 0.90
			print(f'Discounted price: {self.discounted_price:.2f}')
			return self.discounted_price
		else:
			print('You get 15% discount!')
			self.discounted_price = self.total_to_pay * 0.85
			print(f'Discounted price: {self.discounted_price:.2f}')
			return self.discounted_price

	def valid_user_input(valid_options):
		print(f'How many computers do you want? {valid_options}')


'''
	def shipping(self):
		if total_to_pay_after_discount > 10:
			print('Free shipping!')
		else:
			print("Shipping is $4.99")

	def checkout(self):

'''

client1 = Fruitshop()
client1.fill_cart()
client1.price_calculation()
client1.check_discount()

