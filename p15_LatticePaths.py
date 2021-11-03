

def get_ans(positions):
    entangled_relationships_count = positions // 2
    available_entanglements = positions - 1
    valid_configurations_count = 0

    for position in range(0, positions - 1):
        valid_configurations_count += entangled_relationships_count * available_entanglements
        available_entanglements -= 1

    return valid_configurations_count
    
def recur_ans(free_spots):
    if free_spots == 2:
        return 1
    else:
        counter = (free_spots - 1) + recur_ans(free_spots - 2)
        return counter




# Whatever is the most far right, and farthest up (as long as it's not the last right segment) delete it and add 1
if __name__ == "__main__":
    sequence_size = 4
    print(f"Answer to Project Euler problem #15 is: {recur_ans(sequence_size)}")