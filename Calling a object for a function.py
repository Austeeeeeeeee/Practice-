class Light():
	def __init__(self):
		self.is_on = True

	def turn_off_light(self):
		self.is_on = False
		print('The light is being turned off')


class Car():
	def __init__(self,model,year,color):
		self.model = model
		self.year = year
		self.color = color
		self.is_on = True

	def start_engine(self):
		print('Engine started!')

	def end_engine(self):
		print('Engine ended!')

def car_info(car:Car):
	print('Model:', car.model)
	print('Year:', car.year)
	print('Color:', car.color)

my_car = Car('Toyota','2001','blue')

car_info(my_car)
print('\n')

class Book():
	def __init__(self,title,author,year):
		self.title = title
		self.author = author
		self.year = year

def book_info(book:Book):
	print('Title:', book.title,
		  '\nAuthor:', book.author,
		  '\nYear:', book.year)

my_book = Book('Burgos','Antoni','1980')

book_info(my_book)
