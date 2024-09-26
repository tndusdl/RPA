def sumfunc(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num = int(input("1이상 정수를 입력하시오: "))


result = sumfunc(num)
print(f"1부터 {num}까지의 정수의 합은 {result}입니다.")
