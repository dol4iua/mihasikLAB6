
def spiv(h: float, a: int, w: float):
    result = 50 + (0.75 * (h - 150)) + (a - 20) / 4
    print(f'Ваша вага : {w}\nВага необхідна із співвідношення до росту: {result}')
    if abs(w - result) < 3:
        print("Ваша вага в нормі!")
    else:
        print("Ваша вага не в нормі!")


print("Введіть вашу вагу : ", end="")
weight = float(input())
print("\nВведіть ваш зріст : ", end="")
height = float(input())
print("\nВведіть ваш вік : ", end="")
age = int(input())

spiv(height, age, weight)
