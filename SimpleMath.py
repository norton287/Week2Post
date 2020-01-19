# define the simple_addition function to perform the math and return the results
def simple_addition(num1, num2):
    # calculate the sum of num1 + num2
    numbers = num1 + num2
    # return the value in the var numbers
    return numbers


# def main() to start things off
def main():
    # assign result var with the output from the simple_addition function
    result = simple_addition(10, 20)
    # Print the returned result
    print(f'The total was : {result:d}')


# call main
main()
