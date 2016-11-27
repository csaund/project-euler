# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_and_add(limit):
    sum = 0
    for i in range(0, limit):
        by_three = i % 3 == 0
        by_five = i % 5 == 0
        both = by_three == 0 and by_five == 0
        if by_three or by_five and not both:
            sum += i
    return sum


if __name__ == "__main__":
    # test
    # sum = find_and_add(10)
    sum = find_and_add(1000)
    print sum
