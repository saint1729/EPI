def convert_binary_to_int(b):
    ans, bit_position = 0, 0
    while b > 0:
        ans += ((b % 2) * (1 << bit_position))
        b //= 10
        bit_position += 1
    return ans


def convert_int_to_binary(n):
    x = ''
    while n > 0:
        x += str(n % 2)
        n >>= 1
    return x[::-1]