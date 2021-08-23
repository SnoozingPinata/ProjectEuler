

def sum_of_squares(top_number):
    result = 0
    for num in range(0, top_number+1, +1):
        result += num ** 2
    return result

def square_of_sum(top_number):
    sum = 0
    for num in range(0, top_number+1, +1):
        sum += num
    return sum ** 2

def difference_between(num1, num2):
    return abs(num1 - num2)

top_number = 100
sum_of_squares_val = sum_of_squares(top_number)
square_of_sum_val = square_of_sum(top_number)
difference = difference_between(sum_of_squares_val, square_of_sum_val)

print(difference)