# Given a positive integer A, return an array of strings with all the integers from 1 to N.
# But for multiples of 3 the array should have “Fizz” instead of the number.
# For the multiples of 5, the array should have “Buzz” instead of the number.
# For numbers which are multiple of 3 and 5 both, the array should have "FizzBuzz" instead of the number.
def fizzBuzz(A):
    result = []
    for i in range(1, A+1):
        if (not i % 3) and (not i % 5):
            result.append('FizzBuzz')
        elif not i % 3:
            result.append('Fizz')
        elif not i % 5:
            result.append('Buzz')
        else:
            result.append(str(i))

    return result


print(fizzBuzz(15))
