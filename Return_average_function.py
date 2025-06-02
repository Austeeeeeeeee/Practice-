'Writing functions and handeling them in different ways'


###Funtion only does not accept empty lists###
listt = [1,99,56,44,32,9,3,67,8,44,2,6,0,3,55,23,0,3,7,1]
list2 = [1,1,1,1,1,1,1,2]
list3 = []
list4 = [-9,-8]
list5 = [8,2]
list6 = [40,-9]
list7 = [7]


'''

WAYS TO HANDLE ERRORS:
1. RAISE - inside functions - to report real errors (wrong type, empty list, etc) - used for debug and production.
2. ASSERT - checks if conditions is true - for testing code - raises AssertionError,optional error message,
          - stops the program unless try-except is used
          - Can be used in pytest (simple assert) and unittest (self.assertEqual) which is a special method
3. TRY-EXCEPT - outside the function - to handle the error and give the user a nice message.
4. PRINT() only for simple, non-critical info (or temporary debugging).

How raise and try-except are used together?
Raise - throws an error
Try-except - catches and handles it.
'''
def return_average(x:list[int]) -> float:
    if len(x) == 0:
        return 0.0
    return sum(x) / len(x)

print('Returning average number of an list:')

print(return_average(listt))
print(return_average(list2))
print(return_average(list3))
print(return_average(list4))

list_numbers = [3,8,19,33,4,1,7,2,99,6]

def return_max_number(p):
    return max(p)


print('Returning the max number of a list')
print(return_max_number(listt))


#Testing function without frameworks
try:
    print('\nReturning the max number of a list:')
    a = return_max_number(list_numbers)
    print(a)
except (TypeError,ValueError) as error_message:
    print(f'Error:{error_message}')
print('\n')



class Listcalculations:
    def list_sum(l):
        if len(l) == 0:
            raise ValueError ('List cannot be empty')
        if len(l) < 2:
            raise ValueError('List has to contain two numbers!')
        return sum(l)

    def list_division(numbers):
        w = numbers[0]
        r = numbers [1]
        return(w/r)

    def list_multiplication(number):
       a = number [0]
       b = number [1]
       return (a * b)

    def list_substraction(numb):
        assert all(x >= 0 for x in numb), 'Negative numbers are not valid input'
        c = numb[0]
        d = numb[1]
        return c - d


print('Returning sum of the list:')
sum1 = Listcalculations
print(sum1.list_sum(list5))

'''
This is a way to catch and handle an error while calling the function. 
After failing, it will be handled and program continue to run.
'''

try:
    print(sum1.list_sum(list3))
except ValueError as e:
    print(f"Error with list3: {e}")


print(sum1.list_sum(list5))


try:
    print(sum1.list_sum(list7))
except ValueError as u:
    print(f"Error with list7: {u}")

'''


print('\nReturning division of the list:')
div1 = Listcalculations
print(div1.list_division(list5))

print('\nReturning multiplication of the list:')
mul1 = Listcalculations
print(mul1.list_multiplication(list5))

print('\nReturning substraction of the list:')
sub1 = Listcalculations
print(sub1.list_substraction(list5))
print(sub1.list_substraction(list6))
'''





