
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

print("Let's play a game! Think of a number from 0 to 100 and I'll try to guess it!")
print('Is your number lower than 50?')
user_input = input("Enter yes or no: ").strip().lower()

if user_input == 'yes':
    question_even_or_odd = input('Is your number even or odd? ').strip().lower()

    if question_even_or_odd == 'even':
        question_lower_higher_25 = input('Is your number lower or higher than 25? ').strip().lower()
        if question_lower_higher_25  == 'lower':
            first_guess = even_numbers_random_choice(0,25)
            while True:
                answer = input(f'Is your number {next(first_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_25 == 'higher':
            second_guess = even_numbers_random_choice(25,50)
            while True:
                answer = input(f'Is your number {next(second_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

    if question_even_or_odd == 'odd':
        question_lower_higher_25 = input('Is your number lower our higher than 25? ').strip().lower()
        if question_lower_higher_25  == 'lower':
            third_guess = odd_numbers_random_choice(0,25)
            while True:
                answer = input(f'Is your number {next(third_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_25 == 'higher':
            forth_guess = odd_numbers_random_choice(25,50)
            while True:
                answer = input(f'Is your number {next(forth_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break


if user_input == 'no':
    question_even_or_odd = input('Is your number even or odd? ').strip().lower()

    if question_even_or_odd == 'even':
        question_lower_higher_25 = input('Is your number lower or higher than 75? ').strip().lower()
        if question_lower_higher_25  == 'lower':
            first_guess = even_numbers_random_choice(50,75)
            while True:
                answer = input(f'Is your number {next(first_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_25 == 'higher':
            second_guess = even_numbers_random_choice(75,100)
            while True:
                answer = input(f'Is your number {next(second_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

    if question_even_or_odd == 'odd':
        question_lower_higher_25 = input('Is your number lower our higher than 75? ').strip().lower()
        if question_lower_higher_25  == 'lower':
            third_guess = odd_numbers_random_choice(50,75)
            while True:
                answer = input(f'Is your number {next(third_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break

        elif question_lower_higher_25 == 'higher':
            forth_guess = odd_numbers_random_choice(75,100)
            while True:
                answer = input(f'Is your number {next(forth_guess)}? ').strip().lower()
                if answer == 'yes':
                    print('Thanks for playing!')
                    break




