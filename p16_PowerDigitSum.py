

def get_number(number, exponent):
    """Return the power for a given number and a given exponent."""
    return number ** exponent

def tally_characters_of_num(number):
    """Return the total of all characters in a number."""
    number_string = str(number)
    running_total = 0
    for character in number_string:
        running_total += int(character)
    return running_total

def get_ans(number, exponent):
    """Return the answer to p16 for a given number and exponent."""
    big_num = get_number(number, exponent)
    ans = tally_characters_of_num(big_num)
    return ans


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #16 is: {get_ans(2, 1000)}")