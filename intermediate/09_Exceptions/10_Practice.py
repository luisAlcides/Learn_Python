# Custom user-defined exception
class CustomError(Exception):
    def __init__(self, message):
        self.message = message


# Function demonstrating raising an exception
def divide_numbers(a, b):
    try:
        if b == 0:
            raise CustomError('Division by zero is not allowed')
        result = a / b
    except CustomError as e:
        print('Custom exception: ', e.message)

    except ZeroDivisionError:
        print('Error: Division by zero')
    else:
        print('Division successful. Result: ', result)
    finally:
        print('Division operation completed.')


# Main block
try:
    # Example of raising exception and specific exception handling
    num1 = 10
    num2 = 2
    divide_numbers(num1, num2)

    # handling multiple exceptions
    num3 = 10
    num4 = 0
    divide_numbers(num3, num4)

except CustomError as ce:
    print('Custom error handled within main block: ', ce.message)
except ZeroDivisionError:
    print('Error: Division by zero')
except Exception as ex:
    print('An unexpected error ocurred: ', ex)