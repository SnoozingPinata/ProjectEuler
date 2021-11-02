

def is_even(number):
    """Return true if the number given is even. Return False if it is odd."""
    if number % 2 == 0:
        return True
    else:
        return False

def get_next_collatz(number):
    """Return the next number in the Collatz Sequence given a starting number."""
    if is_even(number):
        return number // 2
    else:
        return 3 * number + 1

def gen_collatz_number(starting_number):
    """Generate the next number in the collatz sequence given a starting number."""
    next_num = get_next_collatz(starting_number)
    yield next_num
    while True:
        next_num = get_next_collatz(next_num)
        yield next_num

def add_collatz_que_to_collatz_dict(collatz_queue, offset_value, collatz_dict):
    """Add the collatz_queue values to the collatz_dict."""
    counter = 1
    collatz_queue.reverse()
    for num in collatz_queue:
        sequence_count = counter + offset_value
        collatz_dict.update({num : sequence_count})
        counter += 1
    return collatz_dict

def updated_collatz_dict_with_sequence_starting_at(starting_num, collatz_dict):
    """
    Generate the collatz sequence for a given starting number.
    Add any unknown values to the collatz_dict and return it. 
    """
    assert 1 in collatz_dict
    collatz_queue = []
    gen = gen_collatz_number(starting_num)
    current_num = starting_num
    offset = 0
    while True:
        if current_num in collatz_dict:
            offset = collatz_dict[current_num]
            break
        collatz_queue.append(current_num)
        current_num = next(gen)
    updated_dict = add_collatz_que_to_collatz_dict(collatz_queue, offset, collatz_dict)
    return updated_dict

def parse_dict_for_answer(collatz_dict):
    """Return the key with the highest integer value for the given dictionary."""
    key_list = list(collatz_dict.keys())
    value_list = list(collatz_dict.values())
    max_sequence_count = max(value_list)
    max_value_index = value_list.index(max_sequence_count)
    ans = key_list[max_value_index]
    return ans

def print_percent_complete(progress):
    """Print the calculation percentage status given the solution progress as a fraction."""
    decimal = progress * 100
    status = round(decimal, 2)
    print(f"{status}%")

def find_longest_collatz_sequence_under(max_number):
    """Return the starting number below the given max_number that has the most terms in its collatz sequence."""
    # starting num : sequence count
    # must pre-populate for updated_collatz_dict_with_sequence_starting_at to work right.
    collatz_dict = {1: 1}
    index = 1
    while index < max_number:
        if index not in collatz_dict:
            collatz_dict = updated_collatz_dict_with_sequence_starting_at(index, collatz_dict)
        index += 1
        print_percent_complete(index/max_number)
    return parse_dict_for_answer(collatz_dict)


if __name__ == "__main__":
    max_num = 1000000
    print(f"Answer to Project Euler problem #14 is: {find_longest_collatz_sequence_under(max_num)}")