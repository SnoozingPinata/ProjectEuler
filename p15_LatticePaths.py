

# Whatever is the most far right, and farthest up (as long as it's not the last right segment) delete it and add 1
# This is kind of a hard problem to model... 


def get_unknown_direction_count(sequence_size, known_direction_count):
    return sequence_size - known_direction_count

def get_initial_sequence(sequence_size):
    current_sequence = []
    r_count = sequence_size // 2
    d_count = get_unknown_direction_count(sequence_size, r_count)
    for r in range(0, r_count):
        current_sequence.append('r')
    for d in range(0, d_count):
        current_sequence.append('d')
    return current_sequence

def is_valid_sequence(sequence):
    r_count = sequence.count('r')
    d_count = sequence.count('d')
    if r_count == d_count:
        return True
    else:
        return False

# This won't get all variations. need to improve logic and likely make it keep varying until it finds new sequence (memoization required)
def get_sequence_variation(sequence, initial_sequence):
    r_to_change = sequence.index('r')
    d_to_change = sequence.index('d')
    sequence[r_to_change] = 'd'
    sequence[d_to_change] = 'r'
    if is_valid_sequence(sequence) and sequence != initial_sequence:
        return sequence
    else:
        raise NotImplementedError

def get_valid_sequence_count(sequence_size):
    all_valid_sequences = []
    initial_sequence = get_initial_sequence(sequence_size)
    temp_sequence = initial_sequence.copy()
    all_valid_sequences.append(temp_sequence)
    while True:
        try:
            temp_sequence = get_sequence_variation(temp_sequence, initial_sequence)
            all_valid_sequences.append(temp_sequence)
        except:
            break
    return len(all_valid_sequences)

if __name__ == "__main__":
    sequence_size = 4
    print(f"Answer to Project Euler problem #15 is: {get_valid_sequence_count(sequence_size)}")