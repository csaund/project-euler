import math

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.


def magnitude(x):
     return int(math.log10(x))

def get_digits(number):
    number_list = [int(str(number)[0])]
    for mag in range(magnitude(number), 0, -1):
        number_list.append(int(str(number)[mag]))
    # ugh just explicitly do this.
    # maybe a language isn't great if it's easier to
    # write your own damn split method than use the built in?
    return sorted(number_list)

def test_multiplier(number, multiplier):
    return get_digits(number) == get_digits(number * multiplier)

# lol jk this will never work.
def brute_force(limit, mult_range):
    for i in range(1, limit):
        number_works = True
        for multiplier in range(2, mult_range + 1):
            number_works = number_works and test_multiplier(i, multiplier)
        if number_works:
            return i
    return 0


if __name__ == "__main__":
    # test
    # print get_digits(125874)
    # print test_multiplier(125874, 2)
    # print brute_force(10256, 2)
    # print brute_force(125875, 2)

    print brute_force(1000000, 6)
