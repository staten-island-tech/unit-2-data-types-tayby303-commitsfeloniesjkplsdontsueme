a=int(input("Number 1: "))
b=int(input("Number 2: "))
def find_gcf_loop(num1, num2):
    smaller = min(num1, num2)
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1

print(find_gcf_loop(a, b)
