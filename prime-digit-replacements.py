# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family:
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest
# prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

##
# params:
# num to test if prime
#
# return:
# whether or not number is prime
##
def is_prime(num):
    # shut up.
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

##
# params:
#
# return:
# list of first primes I guess
def generate_primes():


##
# params:
# num to replace digits
# number of digits to replace
# number to replace the digits with
#
# return:
# array of numbers with digits replaced
def get_replaced_digits(num, num_digits_to_replace, replace_with):
    # 56**3 ==> 56003, 56113, 56223 ...
    num_string = str(num)



if __name__ == "__main__":
    # test
    # print is_prime(9)
    get_replaced_digits(56003, 2, 0)
