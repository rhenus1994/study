def is_positive_integer(num):
    return all([isinstance(num, int), num > 0])

def is_prime(num):
    if not is_positive_integer(num):
        raise ValueError("need a positive integer, but '%s' is given" % num)
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return False
    return True
if __name__ == "__main__":
    print(is_prime(4))
    print(is_prime(3))
