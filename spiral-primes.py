# Starting with 1 and spiralling anticlockwise in the following way, a square
#  spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

import math

diagonals = []

# given number spiral, get next n digits
# apends to diagonals as well!
def add_next_n_numbers(spiral, n):
    nums_to_add = []
    for i in range(spiral[-1] + 1, n + 1):
        nums_to_add.append(i)
    diagonals.append(nums_to_add[len(nums_to_add)/2])
    print nums_to_add[len(nums_to_add)/2]

def wrap_spiral():
    # get current side lengths, wrap with one larger
    side_length = int(math.sqrt(len(spiral)))

    print side_length

def make_spiral(side_length):
    numbers = []
    for i in range(1, (int(math.pow(side_length, 2))) + 1):
        numbers.append(i)
    return numbers

# spiral is represented as a list of numbers
# def get_diagonals(spiral):

if __name__ == "__main__":
    # test
    # print make_spiral(3)
    # wrap_spiral()
    spiral = [1, 2, 3, 4]
    add_next_n_numbers(spiral, 9)
    print diagonals
