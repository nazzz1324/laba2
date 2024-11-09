def get_number():
    for i in range(30):
        if i % 2 != 0:
            yield i

ranger = get_number()

s = []
for value in ranger:
    s.append(value)

print("Первое возращенной значение: ", s[0])
print("Пятое возращенной значение: ", s[4])
print("Последнне возращенной значение: ", s[len(s)-1])