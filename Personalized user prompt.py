'''
def ice_cream(message,ice_cream_list):
	joint_list = " or " .join(ice_cream_list)
	print(f'{message} {joint_list}')
	while True:
		user = input().lower()
		if user in [ice.lower() for ice in ice_cream_list]:
			print('Thanks for choosing your ice cream flavour!')
			return user
		else:
			print('Invalid input!Try again')


ice_cream_flavour = ice_cream(f'Choose your ice cream flavour: ', ['Chocolate','Strawberry'])
'''

def cake_flavour():
	cake_flavour = ",".join(['Chocolate','Strawberry','Pineapple','Mango']).lower()
	while True:
		print('Choose your cake flavour:')
		user_input = input().lower()
		if user_input in cake_flavour:
			print(f'Cake flavour chosen --> {user_input}')
		elif user_input not in cake_flavour:
			print('Sorry! We do not have this flavour.')

def cake_size():
	cake_s = [200,400,500]
	while True:
		print('Chose your cake size:')
		user_size = input(int())
		if user_size in cake_s:
			print(f'Cake size --> {user_size}')
		else:
			print('Sorry we do not have this size')
i = cake_flavour()
e = cake_size()
print(i)
print(e)