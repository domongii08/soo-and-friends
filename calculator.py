# 사칙연산 계산기 만들기

def main():
    #사칙연산에 사용할 두 수
    a = 0
    b = 0
    while True:
        try:
            a = int(input('계산할 값 1을 입력하세요'))
        except ValueError: print('올바른 값을 입력하세요')
        break
    while True:
        try:
            b = int(input('계산할 값 2을 입력하세요'))
        except ValueError: print('올바른 값을 입력하세요')
        break

    while True:
        operation = input("연산 방법을 선택하세요(0: 덧셈, 1: 뺄셈, 2: 나눗셈, 3: 곱셈):")
        if operation == '0':
            #print(a+b)
            #break
        elif operation == '1':
            #print(a-b)
            #break
        elif operation == "2":
            #try: print(a/b)
            #except ZeroDivisionError: print("0으로는 나눌 수 없습니다")
            #break
        else:
            #print(a*b)
            #break

if __name__ == '__main__':
    main()
