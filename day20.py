## 함수 선언 부분 ## 
def print_poly(t_x, f_x) -> str:
    poly_expression = "P(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]
        term = t_x[i]

        if (coefficient > 0):
            if(i == 0):
                pass
            else:
                poly_expression += "+"

        elif (coefficient < 0):
            pass

        else:
            continue

        if (term > 0):
            # poly_expression += str(coefficient) + "x^" + str(term) + " "
            poly_expression = poly_expression + f'{coefficient}x^{term} '
        else:
            poly_expression = poly_expression + f'{coefficient}'


    return poly_expression


def calculation_Poly(x_value, t_x, f_x) -> int:
    return_Value = 0

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수
        term = t_x[i]
        return_Value += coefficient * x_value ** term


    return return_Value


## 전역 변수 선언 부분 ## 
fx = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0
tx = [3, 2,  1,  0] # 지수

## 메인 코드 부분 ##
if __name__ == "__main__":

    print(print_poly(tx ,fx))
    print(calculation_Poly(int(input("X 값-->")), tx, fx))



