import time
def factorial(number) -> int:
    '''
    factorial by recursion
    :param number: number (int)
    :return: factorial result (int)
    '''
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def nCr(n, r) -> int:
    '''
    조합 함수
    :param n:
    :param r:
    :return:
    '''
    start = time.time()
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    end = time.time()
    print(f"소요시간 : {end - start:.20f}")
    return int(numerator / denominator)