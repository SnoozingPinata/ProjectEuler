

def order_pythag_triplet(value1, value2, value3):
    """Return an ordered tuple of the given 3 values."""
    values = [value1, value2, value3]
    values.sort()
    return (values[0], values[1], values[2])
    

# Squares the current number, adds the current number to a number list, and the square to a squared list.
# Indices of each list correspond to each other meaning lookups are possible in either direction.
# For each new number, squares it and subtracts each number in the square list. 
# Checks to see if the difference is in the square list as well. If it is, it's a pythag triplet.
# a and b need to be compared and assigned so the output is always (a < b < c).
def gen_pythag_triplet():
    """Generate a valid pythagorean triplet."""
    num_list = [3, 4]
    squared_list = [9, 16]
    while True:
        current_num = num_list[-1] + 1
        current_square = current_num ** 2

        for squared_num in squared_list:
            difference = current_square - squared_num
            if difference in squared_list:
                a = num_list[squared_list.index(difference)]
                b = num_list[squared_list.index(squared_num)]
                yield order_pythag_triplet(a, b, current_num)

        num_list.append(current_num)
        squared_list.append(current_square)


def find_pythag_triplet_product_with_sum(sum):
    """
    Return the product of a * b * c where a, b, and c are members of a pythagorean triplet 
    and where a + b + c is equal to the given sum.
    """
    my_gen = gen_pythag_triplet()
    while True:
        pythag_triplet = next(my_gen)
        total = 0
        ans = 1
        for n in pythag_triplet:
            total += n
            ans *= n
        if total == sum:
            return ans


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #9 is: {find_pythag_triplet_product_with_sum(1000)}")