import random

def even_numbers_random_choice(c, x):
    def unique_even_number_generator(c, x):
        even_numbers = [n for n in range(c, x + 1) if n % 2 == 0]
        random.shuffle(even_numbers)
        for num in even_numbers:
            yield num

    return unique_even_number_generator(c, x)

def odd_numbers_random_choice(x,y):
    def unique_odd_number_generator(c, y):
        odd_numbers = [n for n in range(c, y + 1) if n % 2 != 0]
        random.shuffle(odd_numbers)
        for num in odd_numbers:
            yield num

    return unique_odd_number_generator(x, y)

def get_valid_input(prompt, valid_options):
    valid_options = [opt.lower() for opt in valid_options]
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        formatted = " or ".join(f"'{opt}'" for opt in valid_options)
        print(f"Invalid input! Choose one of the following options: {formatted}")


print("Let's play a game! Think of a number from 0 to 100 and I'll try to guess it!")
print('Is your number lower than 50?')
user_input = get_valid_input("Enter yes or no: ",['yes','no'])

if user_input == 'yes':
    question_even_or_odd = get_valid_input("Is your number even or odd: ",['even','odd'])

    if question_even_or_odd == 'even':
        question_lower_higher_25 = get_valid_input("Is your number lower or higher than 25?: ",['lower','higher'])

        if question_lower_higher_25  == 'lower':
            first_guess = even_numbers_random_choice(0,25)
            while True:
                answer = get_valid_input(f'Is your number {next(first_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_25 == 'higher':
            second_guess = even_numbers_random_choice(25,50)
            while True:
                answer = get_valid_input(f'Is your number {next(second_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

    if question_even_or_odd == 'odd':
        question_lower_higher_25 = get_valid_input("Is your number lower or higher than 25?: ", ['lower', 'higher'])
        if question_lower_higher_25  == 'lower':
            third_guess = odd_numbers_random_choice(0,25)
            while True:
                answer = get_valid_input(f'Is your number {next(third_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_25 == 'higher':
            forth_guess = odd_numbers_random_choice(25,50)
            while True:
                answer = get_valid_input(f'Is your number {next(forth_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break


if user_input == 'no':
    question_even_or_odd = input('Is your number even or odd? ').strip().lower()

    if question_even_or_odd == 'even':
        question_lower_higher_75 = get_valid_input("Is your number lower or higher than 75?: ", ['lower', 'higher'])
        if question_lower_higher_75  == 'lower':
            first_guess = even_numbers_random_choice(50,75)
            while True:
                answer = get_valid_input(f'Is your number {next(first_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_75 == 'higher':
            second_guess = even_numbers_random_choice(75,100)
            while True:
                answer = get_valid_input(f'Is your number {next(second_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

    if question_even_or_odd == 'odd':
        question_lower_higher_75 = get_valid_input("Is your number lower or higher than 75?: ", ['lower', 'higher'])
        if question_lower_higher_75  == 'lower':
            third_guess = odd_numbers_random_choice(50,75)
            while True:
                answer = get_valid_input(f'Is your number {next(third_guess)}? ', ['yes', 'no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_75 == 'higher':
            forth_guess = odd_numbers_random_choice(75,100)
            while True:
                answer = get_valid_input(f'Is your number {next(forth_guess)}? ',['yes','no'])
                if answer == 'yes':
                    print('Thanks for playing!')
                    break




