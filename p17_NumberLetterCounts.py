

num_len_dict = {
    0: 0,
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine")
}

tens_place_number_to_len_dict = {
    0: 0,
    2: len("twenty"),
    3: len("thirty"),
    4: len("forty"),
    5: len("fifty"),
    6: len("sixty"),
    7: len("seventy"),
    8: len("eighty"),
    9: len("ninety")
}

teens_num_len_dict = {
    0: len("ten"),
    1: len("eleven"),
    2: len("twelve"),
    3: len("thirteen"),
    4: len("fourteen"),
    5: len("fifteen"),
    6: len("sixteen"),
    7: len("seventeen"),
    8: len("eighteen"),
    9: len("nineteen")
}

def get_num_character_count(num):
    count = 0

    ones_place = num % 10
    tens_place = (num // 10) % 10
    hundreds_place = (num // 100) % 10
    thousands_place = (num // 1000) % 10

    if thousands_place > 0:
        count += len("thousand")
        count += num_len_dict[thousands_place]

    if hundreds_place > 0:
        count += len("hundred")
        count += num_len_dict[hundreds_place]

    if tens_place == 1:
        count += teens_num_len_dict[ones_place]
    else:
        count += tens_place_number_to_len_dict[tens_place]
        count += num_len_dict[ones_place]

    # accounting for "and"
    if (tens_place or ones_place) and (hundreds_place or thousands_place):
        count += len("and")

    return count

def get_ans(inclusive_top_end):
    assert inclusive_top_end <= 9998
    character_count = 0
    for num in range(1, inclusive_top_end + 1):
        character_count += get_num_character_count(num)
    return character_count


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #17 is: {get_ans(1000)}")