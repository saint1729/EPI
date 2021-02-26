from bit_utilities import *


def right_propagate_rightmost_set_bit(x):
    return x | (x - 1)


if __name__ == '__main__':
    print(convert_int_to_binary(right_propagate_rightmost_set_bit(convert_binary_to_int(1010000))))
