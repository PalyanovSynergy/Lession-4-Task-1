def main():
    # Запрашиваем у пользователя длину и ширину прямоугольника
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    # Вычисляем площадь и периметр
    area = length * width
    perimeter = 2 * (length + width)

    # Выводим результаты
    print(f"Площадь прямоугольника: {area}")
    print(f"Периметр прямоугольника: {perimeter}")

if __name__ == "__main__":
    main()
