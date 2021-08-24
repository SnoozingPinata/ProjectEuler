

# WORK IN PROGRESS

def get_collatz_sequence(number, collatz_sequence):
    if number in collatz_sequence:
        index = collatz_sequence.index(number)
        return collatz_sequence[index: 0]
    elif number % 2 == 0:
        collatz_sequence.append()
        return get_collatz_sequence(number /2, collatz_dict)

sequence = [1, 2, 4, 8, 16, 5, 10]