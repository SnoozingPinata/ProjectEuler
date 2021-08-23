

def is_palindrome(number):
    if isinstance(number, int):
        number = str(number)

    assert isinstance(number, str)

    if len(number) <= 1:
        return True
    elif number[0] != number[-1]:
        return False
    else:
        return is_palindrome(number[1:-1])

def generate_palindrome_list(largest_number):
    palindrome_list = []
    for num in range(largest_number, 0, -1):
        if is_palindrome(num):
            palindrome_list.append(num)
    return palindrome_list

def generate_solutions_list(palindrome_list, first_number, second_number):
    solution_list = []
    for palindrome in palindrome_list:
        for num in range(first_number, 0, -1):
            if palindrome % num == 0:
                if palindrome / num < second_number:
                    solution_list.append(palindrome)
    return solution_list

first_number = 999
second_number = 999
largest_number = first_number * second_number

palindrome_list = generate_palindrome_list(largest_number)
possible_solutions = generate_solutions_list(palindrome_list, first_number, second_number)

possible_solutions.sort()
print(possible_solutions.pop())