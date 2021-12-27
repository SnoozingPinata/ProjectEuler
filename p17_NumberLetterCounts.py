

ones_place_number_to_len_dict = {
    0: 0, #Not counted**
    1: 3, #one
    2: 3, #two
    3: 5, #three
    4: 4, #four
    5: 4, #five
    6: 3, #six
    7: 5, #seven
    8: 5, #eight
    9: 4 #nine
}

tens_place_number_to_len_dict = {
    0: 0, #Not counted**
    1: 4, #teen
    2: 6, #twenty
    3: 6, #thirty
    4: 6, #fourty
    5: 5, #fifty
    6: 5, #sixty
    7: 7, #seventy
    8: 6, #eighty
    9: 6 #ninety
}

special_nums_number_to_len_dict = {
    10: 3, #ten
    11: 6, #eleven
    12: 6, #twelve
    13: 8, #thirteen
    15: 7 #fifteen
}

def is_thousand(num):
    if num > 999:
        return True
    else:
        return False

def is_hundred(num):
    if num > 99:
        return True
    else:
        return False

def is_ten(num):
    if num > 9:
        return True
    else:
        return False

def is_special_case(num):
    special_case_list = [10, 11, 12, 13, 15]
    string_of_num = str(num)
    num_last_two_digits = string_of_num[-2] + string_of_num[-1]
    if int(num_last_two_digits) in special_case_list:
        return True
    else:
        return False

def get_num_character_count(num):
    current_num_letter_count = 0
    current_num_string = str(num)
    if is_thousand(num):
        current_num_letter_count += 8 #thousand
        current_num_letter_count += ones_place_number_to_len_dict[int(current_num_string[-4])]
    if is_hundred(num):
        current_num_letter_count += 7 #hundred
        current_num_letter_count += ones_place_number_to_len_dict[int(current_num_string[-3])]
    if is_ten(num):
        if is_special_case(num):
            last_two_digits_string = current_num_string[-2] + current_num_string[-1]
            current_num_letter_count += special_nums_number_to_len_dict[int(last_two_digits_string)]
        else:
            current_num_letter_count += tens_place_number_to_len_dict[int(current_num_string[-2])]
            current_num_letter_count += ones_place_number_to_len_dict[int(current_num_string[-1])]
    else:
        current_num_letter_count += ones_place_number_to_len_dict[int(current_num_string[-1])]
    return current_num_letter_count

def get_ans(inclusive_top_end):
    assert inclusive_top_end <= 9998
    max_number = inclusive_top_end + 1
    character_count = 0
    for num in range(1, max_number):
        character_count += get_num_character_count(num)
    return character_count


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #17 is: {get_ans(1000)}")