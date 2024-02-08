import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"소요시간 : {end - start:.20f}")
        return result
    return wrapper






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


@timer
def nCr(n, r) -> int: #SRP 준수
    '''
    조합 함수
    :param n:
    :param r:
    :return:
    '''

    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)

    return int(numerator / denominator)



