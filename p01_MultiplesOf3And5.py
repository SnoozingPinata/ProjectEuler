

def sum_of_multiples_below(upper_bound, multiples):
    """
    Find the sum of all numbers below the upper_bound that are a multiple of any multiple in the given list.

    upper_bound: The upper bound for any number to be included in the sum.

    multiples: An iterable containing integers. A number must be a product of one of the members of the list to be added to the sum.
    """
    counter = 0
    running_total = 0
    while counter < upper_bound:
        for multiple in multiples:
            if counter % multiple == 0:
                running_total += counter
                break
        counter += 1
    return running_total


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #4 is: {sum_of_multiples_below(1000, [3, 5])}")