import triangle

side1 = float(input("Введите сторону a: "))
side2 = float(input("Введите сторону b: "))
side3 = float(input("Введите сторону c: "))

area = triangle.heron_formula(side1, side2, side3)

print(f"Площадь треугольника: {area:.2f} ")

