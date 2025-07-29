import random
from dataclasses import dataclass

print('----------------- PART 1: CREATING A GLOBAL GENERATOR -----------------')
@dataclass
class ZOOM_TYPES:
    MINIMUM = 0
    RANDOM = 1
    MAXIMUM = 2

def set_max_zoom() -> int:
    maximum_value = 30000
    return maximum_value

def unique_random_zoom_generator(start=50, end=150):
    zoom_values = list(range(start, end + 1))
    random.shuffle(zoom_values)
    for zoom in zoom_values:
        yield zoom

def set_random_zoom_value(zoom_value: int) -> None:
    print(f"Setting random zoom to {zoom_value}")

def check_zoom_after_reboot(zoom_generator, zoom_type=ZOOM_TYPES.RANDOM):
    if zoom_type == ZOOM_TYPES.MAXIMUM:
        max_zoom = set_max_zoom()
        print(f"Setting max zoom: {max_zoom}")
    else:
        random_zoom_value = next(zoom_generator)
        set_random_zoom_value(random_zoom_value)

# Create generator once
#This method will not allow any repeats, as you are using the same generator each time you call the function.
zoom_gen = unique_random_zoom_generator()

# Call with zoom_gen and zoom_type
check_zoom_after_reboot(zoom_gen, zoom_type=ZOOM_TYPES.RANDOM)
check_zoom_after_reboot(zoom_gen, zoom_type=ZOOM_TYPES.RANDOM)
check_zoom_after_reboot(zoom_gen, zoom_type=ZOOM_TYPES.RANDOM)



print('----------------- PART 2: CREATING A GLOBAL GENERATOR -----------------')
print('Grouping numbers into odd or even')
def unique_number(start=1, end=21):
    list_of_numbers = list(range(start,end))
    random.shuffle(list_of_numbers)
    for number in list_of_numbers:
        if number % 2 == 1:
            yield f'This number {number} is odd.'
        elif number % 2 == 0:
            yield f'This number {number} is even.'


gen = unique_number()
while True:
    try:print(next(gen))
    except StopIteration:
        print('No more numbers!')
        break


print()
print('----------------- Part 3: CREATING A GLOBAL GENERATOR -----------------')
print('Random discount codes')

def random_code(prefix="SUMMER",start = 1, end = 10):
    numbers = list(range(start,end + 1))
    random.shuffle(numbers)
    for number in numbers:
        yield f'{prefix}{number}'

#It created a generator objected but it does not run it
generating_disocunt_code = random_code()

while True:
    try:
        print(next(generating_disocunt_code))
        #Run the function
        #Runs the code until it hits the first yield
        #Returns the value
        #Pause and wait for the next() call.
    except StopIteration:
        print('No mode discount codes!')
        break


print()
print('----------------- Part 4: CREATING A GLOBAL GENERATOR -----------------')
print('Classifying numbers into lower or higher then 25. Using pass to loop.')

def print_when_2(start = 1,end = 51):
    numbers = list(range(start,end))
    random.shuffle(numbers)
    for n in numbers:
        if n <= 25:
            print(f'Lower than 25 - {n}')
            yield n
        elif n >= 25:
            print(f'Higher than 25 - {n}')
            yield n



gene = print_when_2()
for g in gene:
    pass

print()
print('------------- CREATING NEW GENERATOR WITH EACH FUNCTION CALL -----------------------')
import random
from dataclasses import dataclass

@dataclass
class ZOOM_TYPES:
    MINIMUM = 0
    RANDOM = 1
    MAXIMUM = 2

def set_max_zoom() -> int:
    maximum_value = 30000
    return maximum_value

def unique_random_zoom_generator(start=0, end=100):
    zoom_values = list(range(start, end + 1))
    random.shuffle(zoom_values)
    for zoom in zoom_values:
        yield zoom

def set_random_zoom_value(zoom_value: int) -> None:
    print(f"Setting random zoom to {zoom_value}")

def check_zoom_after_reboot(zoom_type=ZOOM_TYPES.RANDOM):
    if zoom_type == ZOOM_TYPES.MAXIMUM:
        max_zoom = set_max_zoom()
        print(f"Setting max zoom: {max_zoom}")
    else:
        zoom_generator = unique_random_zoom_generator()
        random_zoom_value = next(zoom_generator)
        set_random_zoom_value(random_zoom_value)

#You create a new generator everything you call this function, which may result in repeated numbers
check_zoom_after_reboot(ZOOM_TYPES.RANDOM)

