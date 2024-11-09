import random

s=[]

for k in range(0, random.randint(10, 15)):
        n = random.randint(0, 200)
        while True:
            if n not in s:
                s.append(n)
                break
            else:
                n = random.randint(0, 200)

x = input("Введите цифру X (от 1 до 9): ")

if x.isdigit() and len(x) == 1:
    x = int(x)
    if x == 0:
        print("Цифра не должна быть равна нулю.")

result = list(filter(lambda num: num % x == 0, s))
result = ', '.join(str(item) for item in result)

print(f"Все найденные числа, кратные {x}: ", result)
