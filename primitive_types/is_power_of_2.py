def is_power_of_2(x):
    return x != 0 and (x & (x - 1) == 0)


if __name__ == '__main__':
    print(is_power_of_2(64))
    print(is_power_of_2(63))
