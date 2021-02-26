def x_mod_a_power_of_2(x, y):
    return x & (y - 1)


if __name__ == '__main__':
    print(x_mod_a_power_of_2(77, 64))