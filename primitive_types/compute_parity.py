from primitive_types.bit_utilities import convert_binary_to_int, convert_int_to_binary


def compute_parity(x):
    parity = 0
    while x != 0:
        parity ^= (x & 1)
        x >>= 1
    return parity


def compute_parity_eff_1(x):
    parity = 0
    while x != 0:
        parity ^= 1
        x &= (x - 1)
    return parity


def compute_parity_eff_2(x):
    x ^= (x >> 32)
    x ^= (x >> 16)
    x ^= (x >> 8)
    x ^= (x >> 4)
    x ^= (x >> 2)
    x ^= (x >> 1)
    return x & 1


if __name__ == "__main__":
    # print(convert_binary_to_int(1001))
    print(compute_parity(convert_binary_to_int(11110111)))
    print(compute_parity_eff_1(convert_binary_to_int(11110111)))
    print(compute_parity_eff_2(convert_binary_to_int(11110111)))
    print(0xFFFF)
    print(2**16-1)
    print(15 * 16**0 + 15 * 16**1 + 15 * 16**2 + 15 * 16**3)
    print(convert_int_to_binary(77))
    print(convert_int_to_binary(64))
    print(convert_int_to_binary(4))
    print(77 & (64 - 1))