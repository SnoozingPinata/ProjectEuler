

def gen_pythag_triplet():
    num_list = [3, 4]
    squared_list = [9, 16]
    while True:
        new_num = num_list[-1] + 1
        new_square = new_num ** 2

        for squared_num in squared_list:
            a_squared = new_square - squared_num
            if a_squared < squared_num < new_square:
                if a_squared in squared_list:
                    a = num_list[squared_list.index(a_squared)]
                    b = num_list[squared_list.index(squared_num)]
                    c = new_num
                    yield (a, b, c)
        num_list.append(new_num)
        squared_list.append(new_square)

my_gen = gen_pythag_triplet()

while True:
    pythag_triplet = next(my_gen)
    total = 0
    ans = 1
    for n in pythag_triplet:
        total += n
        ans *= n
    if total == 1000:
        print("Pythag Triple Special Product: " + str(ans))
        break