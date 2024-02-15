def palindrome(s):

    if len(s) <= 1:
        return True

    if s[0] != s[len(s)-1]:
        return False

    return palindrome(s[1:len(s)-1])


str_array = ['reaver', 'kayak', 'Borrow or rob', '주유소의 소유주', '야 너 이번주 주번이 너야', '살금 살금']


for s in str_array:
    print(f'{s} --> ',end ='')
    s = s.lower().replace(' ', '')
    if palindrome(s):
        print('symmetric')

    else:
        print('asymmetric')


