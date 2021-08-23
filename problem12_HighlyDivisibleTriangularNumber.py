

def gen_triangular_number():
    counter = 0
    triangle_num = 0
    while True:
        counter += 1
        triangle_num += counter
        yield triangle_num

# this isn't actually used, but I needed it to test the get_factor_count function
def get_factors(number):
    if number == 1:
        return ([1], 1)
    factors = [1, number]
    lower_bound = 2
    upper_bound = number
    count = 2
    while lower_bound < upper_bound:
        if number % lower_bound == 0:
            factors.append(lower_bound)
            upper_bound = int(number / lower_bound)
            factors.append(upper_bound)
            count +=2
        lower_bound += 1
    return (factors, count)

# This is the same function as above, but it doesn't keep track of the factors, just the count.
# Just an optimization of the above for this specific problem. 
# Key part is to lower the upper bound for every factor you find.
def get_factor_count(number):
    lower_bound = 2
    upper_bound = number
    count = 2
    while lower_bound < upper_bound:
        if number % lower_bound == 0:
            upper_bound = int(number / lower_bound)
            count +=2
        lower_bound += 1
    return count


gen = gen_triangular_number()
next(gen)
highest_count = 0
max_factor_count = 500

while True:
    triangle_num = next(gen)
    count = get_factor_count(triangle_num)
    if count > highest_count:
        # This is just so you can see the progress. The entire if statement is unnecessary. 
        print(f"New Highest Count: {count}. ({triangle_num})")
        highest_count = count
    if count > max_factor_count:
        break

print("Answer is : " + str(triangle_num))