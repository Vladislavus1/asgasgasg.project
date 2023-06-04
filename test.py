import time
kilos = 0.45
inches = 2.54
def func(a, b, magnitude):
    for i in range(a, b + 1):
        print(f'{i}        {i * magnitude}')
#1
print("Фунти.    Кілограми.")
func(1, 50, kilos)
#2
print("Дюйми.    Сантиметри.")
func(1, 50, inches)
#3
print("Сума цілих чисел від 1 до n")

n = int(input("n ="))

suma = 0
for i in range(1, n+1):
    time.sleep(0.2)
    print("Сума чисел від 1 до", n, " = ", suma)
    time.sleep(0.2)
    print("Додаємо число", i, "suma = ", suma)



