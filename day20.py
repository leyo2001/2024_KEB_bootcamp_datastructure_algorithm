## 함수 선언 부분 ## 
def print_poly(f_x) -> str:
    term = len(f_x) - 1     # 최고차항 숫자 = 배열길이-1
    poly_expression = "P(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수

        if (coefficient > 0):
            if(i == 0):
                pass
            else:
                poly_expression += "+"

        elif (coefficient < 0):
            pass

        else:
            term -= 1
            continue

        if (term > 0):
            # poly_expression += str(coefficient) + "x^" + str(term) + " "
            poly_expression = poly_expression + f'{coefficient}x^{term} '
        else:
            poly_expression = poly_expression + f'{coefficient}'



        term -= 1

    return poly_expression


def calculation_Poly(x_value, f_x) -> int:
    return_Value = 0
    term = len(f_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수
        return_Value += coefficient * x_value ** term
        term -= 1

    return return_Value


## 전역 변수 선언 부분 ## 
fx = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":

    print(print_poly(fx))
    print(calculation_Poly(int(input("X 값-->")), fx))



