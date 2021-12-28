

def is_sunday(day_count):
    # jan 1, 1900 is a monday so we know that every date that is divisible by 7 is a sunday
    # if a different starting day was given, we'd have to adjust the 7 to match
    if day_count % 7 == 0:
        return True
    else:
        return False

def is_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True

def update_month_day_count_map(month_day_count_map, is_leap_year):
    updated_map = month_day_count_map.copy()
    if is_leap_year:
        updated_map[1] = 29
    else:
        updated_map[1] = 28
    return updated_map

def get_ans():
    month_day_count_map = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day_counter = 0
    answer_counter = 0

    for year in range(1900, 2001):
        month_day_count_map = update_month_day_count_map(month_day_count_map, is_leap(year))
        for month_index in range(0, len(month_day_count_map)):
            for day_of_month in range(0, month_day_count_map[month_index]):
                total_day_counter += 1
                if year > 1900:
                    if is_sunday(total_day_counter) and day_of_month == 0:
                        answer_counter += 1
    return answer_counter


if __name__ == "__main__":
    print(f"Answer to Project Euler problem #19 is: {get_ans()}")